from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from crm.models import tbl_lead, master_company
from django.shortcuts import get_object_or_404
from crm.utils import send_whatsapp_message  # Adjust as per your project

class Command(BaseCommand):
    help = 'Send WhatsApp reminders for tomorrow\'s meetings'

    def handle(self, *args, **kwargs):
        tomorrow = datetime.now().date() + timedelta(days=1)
        leads = tbl_lead.objects.filter(
            next_meeting_date__date=tomorrow,
            status="Meeting"
        )

        for curr_data in leads:
            ph_no = str(curr_data.mobile).strip()
            company_obj = get_object_or_404(master_company, com_id=curr_data.company_id)
            company_name = company_obj.com_name.title()
            lead_name = curr_data.c_name.title()
            meeting_date_str = curr_data.next_meeting_date.strftime('%d-%m-%Y | %I:%M %p')

            send_whatsapp_message(
                ph_no,
                message_type='template',
                template_name='meeting_message',
                template_params=[company_name, lead_name, meeting_date_str]
            )

        self.stdout.write(self.style.SUCCESS("Meeting reminders sent successfully."))

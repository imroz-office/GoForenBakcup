from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
import mysql.connector

class CheckUserIsActiveMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user_id = request.session.get('session_id')
        if user_id:
            cnx = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='shubhamsingh_sit_crm'
            )
            # cnx = mysql.connector.connect(
            #     user='shubhamsingh_sit_crm',
            #     password='kish@1102',
            #     host='localhost',
            #     database='shubhamsingh_sit_crm'
            # )
            cursor = cnx.cursor(dictionary=True)
            cursor.execute('SELECT is_active FROM tbl_users2 WHERE userId = %s', (user_id,))
            user = cursor.fetchone()
            cursor.close()
            cnx.close()

            if not user or not user.get('is_active'):
                request.session.flush()
                return redirect('login')  # Ensure this URL name is defined in your urls.py

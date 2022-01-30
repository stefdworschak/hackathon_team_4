from datetime import datetime, date
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from wellbeing.models import Mood


class DatePickerView(View):
    '''
    Date picker that allows the user to choose which day to display
    successfull url redirects to the page where url contains date
    '''
    template_name = "reporting/date_picker.html"

    def get(self, request, *args, **kwargs):
        '''
        gets page that displays a html form
        '''
        return render(request, 'reporting/date_picker.html')

    def post(self, request, *args, **kwargs):
        '''
        posts date picker form data
        '''
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        # need to add one day to end date ???
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, id=user_id)
        mood_objects_list = Mood.objects.filter(created_on__range=[start_date, end_date]).filter(author=user)
        list_of_dates = []
        list_of_dates_strings = []
        for object in mood_objects_list:
            datetime_object = object.created_on
            date_to_string = datetime_object.strftime("%d %B %Y")
            if date_to_string not in list_of_dates_strings:
                list_of_dates_strings.append(date_to_string)
                list_of_dates.append(datetime_object)

            # unique_dates_list = list(set(list_of_dates))

        # print(f'LIST OF UNIQUE DATETIME OBJECTS{list_of_dates}')
        # print(f'LIST OF UNIQUE strings {list_of_dates_strings}')
        for date in list_of_dates:
            moods_objects_on_day = Mood.objects.filter(created_on=date)
            list_of_moods_in_one_day = []
            for objects in moods_objects_on_day:
                mood = object.mood
                if mood not in list_of_moods_in_one_day:
                    list_of_moods_in_one_day.append(mood)


            print(f'THIS IS ONE DATE{date}')
            print(f'LIST OF MOODS IN ONE DAY {list_of_moods_in_one_day}')
            


        # context = {
        #     start_date = start_date
        #     end_date = end_date
        # }
        # return redirect("reports:mood_report", context)
        return render(request, 'index.html')


def get_mood_report_page(request):
    """ View to get mood report page """
    return render(request, 'reporting/mood_report.html')


def get_test_404_page(request):
    """ View to get 404 page page """
    return render(request, '404.html')

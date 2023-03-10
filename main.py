import requests


### FUNCTION TO CALL THE API AND STORE RESULTS IN A JSON FILE ###
def get_json_file():
   get_author = requests.get("https://dev.ylytic.com/ylytic/test")
   data = get_author.json()

   import json
   with open('db.json','w',encoding='utf8') as f:
      json.dump(data,f,ensure_ascii=False,indent=4)
   
   comments = data['comments']

   return comments


### CALLING FUNCTION TO RETREIVE DATA ###
comments = get_json_file()



### TASK 1 -> SEARCHING COMMENTS WITH AUTHOR NAME ###
def search_by_author(author_name):
   result = [] # for storing final result
   # matching with given author name
   for comment in comments:
      if comment['author'] == author_name:
         result.append(comment['text'])

   # returning result
   return result

## UNCOMMENT BELOW LINES TO search by author name 
## taking 'Dan noringer' as example here
# print("All comments by Dan noringer")
# for items in search_by_author("Dan noringer"):
#    print(items)
# print('\n\n')



### TASK 2 -> SEARCHING COMMENTS BY DATA RANGE ###
def search_by_date(start_year = '2023',start_month = 'Jan',start_date = '1',end_year = '2023',end_month = 'Feb',end_date = '1'):
   result = [] # for final result

   # importing required modules
   from datetime import datetime
   from time import strftime

   # coverting to required format
   startDate = datetime.strptime(f'{start_month} {start_date} {start_year}', '%b %d %Y')
   endDate = datetime.strptime(f'{end_month} {end_date} {end_year}', '%b %d %Y')

   # parsing to get values
   for comment in comments:
      temp_date = comment['at']
      s = temp_date.split()
      # the date of the current comment in the loop
      currentCommentDate = datetime.strptime(f'{s[2]} {s[1]} {s[3]}', '%b %d %Y')
      # checking if it is between start and end dates
      if startDate < currentCommentDate < endDate:
         result.append(comment['text'])

   return result


### UNCOMMENT BELOW LINES TO SEARCH COMMENTS BY DATE
### a default value is given which can be changed if needed
# for items in search_by_date():
#    print(items)
# print('\n\n')


### TASK 3 -> SEARCHING COMMENTS WITHING A CERTAIN RANGE
### FOR NUMBER OF REPLIES AND NUMBER OF LIKES
def range_for_like_replies(start_like=0, end_like=5,start_replies=0,end_replies=5):
   result = [] # for final result

   for comment in comments:
      if (start_replies <= comment['reply'] <= end_replies) and (start_like <= comment['like'] <= end_like):
         result.append(comment['text'])

   return result

### UNCOMMENT BELOW LINES FOR
### THE ABOVE FUNCTION
# for items in range_for_like_replies():
#    print(items)
# print('\n\n')


### TASK 4 -> SEARCHING COMMENTS WITH SEARCH STRING IN THE TEXT FIELD
def search_text(text = 'economic'):
   result = [] # for final result

   for comment in comments:
      if text in comment['text']:
         result.append(comment['text'])

   return result

## UNCOMMENT TO ACCESS ABOVE FUNCTION
# for item in search_text():
#    print(item)


### TASK 5 -> ACCESS ALL 4 ABOVE
def call_all(author_name = 'Dan noringer',start_year = '2023',start_month = 'Jan',start_date = '1',end_year = '2023',end_month = 'Feb',end_date = '1',start_like=0, end_like=5,start_replies=0,end_replies=5,text = 'economic'):
   ### have provided some default values to the function
   ### so that it can be called and tested with ease
   ## calling all 4 functions above
   commentsByAuthors = search_by_author(author_name)
   commentsBYDate = search_by_date(start_year,start_month,start_date,end_year,end_month,end_date)
   commentsByLikeReplies = range_for_like_replies(start_like,end_like,start_replies,end_replies)
   commentsByText = search_text(text)

   result = [] # for stroring result

   ## seeing for common ones
   for comment in commentsByAuthors:
      if comment in commentsBYDate and commentsByLikeReplies and commentsByText:
         result.append(comment)

   return result


### UNCOMMENT TO ACCESS ABOVE FUNCTION
for item in call_all():
   print(item)
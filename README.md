# Good-READS
Breakdown and build up project. To understand the working of Django forms, class based views, handling of static files and settings core functions.


## Two main apps: Accounts and Books
### Accounts: 
Managing the acount related stuf, login, account created, account model. User account model design and similar account related functions.

### Books: 
Listing out all the available books with auther details and a short description. Authenticated users can then request a lend on the books. 

### Account_Templates:
Two templates, login and signup with the basic sigin and signup functionality. CSS in static files to design. 

### Book_Templates:
Book home page to list all the available books. Main css for home. 

## Problems: 
1. CSS Grid is missing some property, does not cover whole page.
2. Fontsize for the content is too small
3. Absolute footer position is overlapped by CSS grid when there are more rows. 

## Static File structure
For each apps, static files resides insides the static/app/ folder. For example, the css files for accounts app shall be available in accounts/static/account/css/signup.css
'collectstatic' will collect all files from these apps and will put them in project static folder. This is only for deployment but a good practise. 
STATIC_ROOL = 'static', collectstatic will put all static files in here. 

## Templates File Structure
For each apps, template files(html) resides insides the templates/app/ folder. Considering the index html file in books app,
books/templates/books/index.html


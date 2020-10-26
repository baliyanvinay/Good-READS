## Problems: 
- Absolute footer position is overlapped by CSS grid when there are more rows: Parked
- Header does not highlight the active link; Need to active for the current page.
- Form Invalid validation error does not display any error messages: Parked

## Enhancements:
1. Authors - Authors shall be registered users but with isAuthor flag set to True; Only the authors shall be displayed on the author page. 
2. Registered users can lend a book only if the shelf has a copy of the book available. 
3. Registered users can add a book if they like and also can delete the ones they have added. 
4. Admin user or Super user can add/remove a user/book from the admin panel.
5. Registered user can view their profile and can make themselves author at any time. 
6. Author can't be a user if there are books linked to him/her. Books must be deleted first. 

# Good-READS
Breakdown and build up project. To understand the working of Django forms, class based views, handling of static files and settings core functions.


## Two main apps: Accounts and Books
### Accounts: 
Managing the acount related stuf, login, account created, account model. User account model design and similar account related functions.
Forms.py: CreateUserView to create user accounts | 
Views.py: FormView to register user & save data |

### Books: 
Listing out all the available books with auther details and a short description. Authenticated users can then request a lend on the books. 

### Account_Templates:
Two templates, login and signup with the basic sigin and signup functionality. CSS in static files to design. 

### Book_Templates:
Book home page to list all the available books. Main css for home. 

## Static File structure
For each apps, static files resides insides the static/app/ folder. For example, the css files for accounts app shall be available in accounts/static/account/css/signup.css
'collectstatic' will collect all files from these apps and will put them in project static folder. This is only for deployment but a good practise. 
STATIC_ROOL = 'static', collectstatic will put all static files in here. 

## Templates File Structure
For each apps, template files(html) resides insides the templates/app/ folder. Considering the index html file in books app,
books/templates/books/index.html

## Model Design
### Book
- title
- genre(Many-to-Many with Genre)
- author(foreign key of Accounts)
- copies
- date_added
- ratings
- short_desc
- description
- cover_picture

### Genre
- name

### Accounts
- is_author
- picture
- user(AbstractUser)
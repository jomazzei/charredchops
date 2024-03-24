<p align="center"><img src="/DocAssets/mock-up.png"></p>
<hr>

<h1 align="center">Charred Chops</h1>

[View live deployment here!](https://jomazzei-charred-chops-161a869d9d8b.herokuapp.com/)

<p>This website project is for a hypothetical steakhouse, Charred Chops, with the main goal of offering a user friendly manner to book and manage a reservation with the restaurant.</p>
<p>In future the features of the application will scale beyond just user reservation, also offering the staff a way to manage the displayed menu and manage all customer bookings</p>

<hr>

<br>


#### Table of Contents:

* [Agile, Project Management and Tech Stack Overview](#agile-project-management-and-tech-stack-overview)
  * [Ideation and Agile](#ideation-and-agile)
  * [Project Management and Version Control](#project-management-and-version-control)
  * [Tech Stack](#tech-stack)

* [Wireframes and Database Schema](#wireframes-and-database-schema)
  * [Home page](#home-page)
  * [Booking page](#booking-page)
  * [My Bookings page](#my-bookings-page)
  * [Reservation Detail page](#reservation-detail-page)
  * [Database diagram](#database-diagram)
  * [Changes to the Reservation model](#changes-to-the-reservation-model)

* [User Stories and Features](#user-stories-and-features)
  * [Full Layout of Milestones](#full-layout-of-milestones)
  * [Core Focus](#core-focus)
  * [Future focus](#future-focus)

* [Current Key User Story Implementations](#current-key-user-story-implementations)
  * [USER STORY: Contact and location info](#user-story-contact-and-location-info)
  * [USER STORY: Account creation / login](#user-story-account-creation-and-login)
    *  [Sign Up](#sign-up)
    *  [Log In](#log-in)
    *  [Log Out](#log-out)
  * [USER STORY: Book a table](#user-story-book-a-table)
  * [USER STORY: View own bookings](#user-story-view-own-bookings)
    * [List View](#list-view)
    * [Detail View](#detail-view)
  * [USER STORY: Edit reservation details](#user-story-edit-reservation-details)
  * [USER STORY: Cancel booking](#user-story-cancel-booking)
  * [Toast feedback message](#toast-feedback-message)
    * [Create Booking](#create-booking)
    * [Update Booking](#update-booking)
    * [Cancel Booking](#cancel-booking)
    * [Error](#error)

* [Validation and Testing](#validation-and-testing)
  * [Validation](#validation)
  * [Performance and Contrast Tests](#performance-and-contrast-tests)
  * [Testing table](#testing-table)  
  * [Test Module and Debugging](#test-module-and-debugging)

* [Forking](#forking)

* [Credits](#credits)
  * [Images](#images)
  * [Content and Code](#content-and-code)
  * [Note on ChatGPT](#note-on-the-use-of-chatgpt-for-coding-related-queries)
* [Thank you](#a-thank-you)

<br>  


## Agile, Project Management and Tech Stack Overview
[back to content table](#table-of-contents)

<br>

### Ideation and Agile
<p>
 During the ideation process for choosing a project I referred to the briefs on the CI LMS. I ended up choosing the restaurant booking system as the outline for my project.
 I did some quick brainstorming for names and wrote out baseline user stories, whether those be current or future iterations, that informed the core features of the website.<br>
</p>
<p>
 Throughout development I would add more user stories to my project board that would expand the website's functionality and enrich it's value, while ensuring I maintained a focussed scope and goal for this deadline<br>
 I split certain features into easier to track issues or task checklists depending on whether they were explicitly part of a user story or not.<br>
 Certain design aspects would fit into that category, such as error pages. They could have been rephrased and reworked into more stories but I felt it would take away from the main focus
 of agile, which is to inform scope and promote efficiency throughout an iteration through breaking down tasks.
</p>

<br>

#### Project Management and Version Control
<p>
 To manage my development and deployment smoothly I seperated those 2 key components of the app's life cycle into their own branches.<br>
 This gives me more control over updating certain features, being able to cut out unfinished features or bugged code from the deployed version of the website without having to comment and uncomment entire sections of my project every time I update the deployment for a finished feature.<br>
</p>
<p>
 This was very helpful at the start when having to work on multiple elements at once as they were all co-dependent on eachother. Going back and forth introduced some bugs but being able to dedicate a branch specifically to a streamlined version was helpful in this process.
</p>
<p>
 For further protection against introducing unwanted bugs and non-functional code I created a 3rd merge branch.<br>
 In effect, this is just an extra step between merging branches directly and using commits as a back up, arguably this might muddy the development when git has built in functionality to handle these steps.<br>
 The reason I chose this way regardless was for an extra layer of protection for my Stable branch, providing an extra back up where I can locally test the combined branches without having to rerun commit restores and re-pulling the branches if there's a mistake.<br>
 So while it is an extra step, for my process it streamlined testing.<br>
</p>
<p>
 I think my approach worked for a 1-person project, as there was no need for the more standard "branch-per-feature" common in a larger team where everyone is developing mostly isolated features.
</p>

<br>

### Tech Stack
<p>
 The following high level technologies and frameworks were used to deliver the project in it's current state:
</p>

- __Ideation, project management and version control__
  - Lucidchart - Entity relationship diagram
  - Balsamiq - Wireframes sketching tool
  - VS Code - Text editor / IDE
  - GitHub - Version control system / online code repository

- __Frontend__
  - HTML5 & CSS3 - Content and design
  - Bootstrap 5 - Framework for fast design elements
  - JavaScript - Interactivity

- __Backend__
  - Python 3.12 - Base language for Django
  - Django 4.2 - Framework for rapid creation of database-reliant web applications
  - ElephantSQL - Database hosting service

- __Deployment__
  - Heroku - Full-stack web application hosting service

<p>
 For a detailed list of package usage and requirements, please see the requirements.txt.
</p>

<br>


## Wireframes and Database schema
[back to content table](#table-of-contents)

<br>

### Home Page
![home](/DocAssets/home-fresh-view.png)

<br>

### Booking Page
![bookingpage](/DocAssets/booking-logged-in.png)

<br>

### My Bookings Page
![listview](/DocAssets/bookings-list-view.png)

<br>

### Reservation Detail Page
![detailview](/DocAssets/detailed-booking-view.png)

<br>

### Database Diagram
![database](/DocAssets/lucidchart-schema.png)

#### Changes to the Reservation model

<p>
 I drew out the model quite broadly initially, more fitting to a larger scope and longer iteration.<br>
 During the prioritization I narrowed down the model quite a bit to focus more on the key feature of booking a reservation.<br>
 This is the current working version of the model in diagram form:
</p>

![database-working](/DocAssets/working-version-schema.png)

<br>

<br>

## User Stories and Features
[back to content table](#table-of-contents)
<br>
<br>

### Full Layout of Milestones

- __Reservation__
  - USER STORY: Book a table:
    - As a user I want to book a table so that I can secure a reservation.
  - USER STORY: View own bookings:
    - As a user I can access my own bookings so that I can edit their details, cancel them, or just view them.
  - USER STORY: Edit reservation details:
    - As a user I want to be able to change specifics about my reservation so that I can reschedule or tweak the guest count to suit my needs.
  - USER STORY: Cancel booking:
    - As a user I want to be able to cancel a booking so that I can change the schedule of my plans / let the restaurant know I won't be showing up.
  - USER STORY: E-mail booking confirmation:
    - As a user I want to receive email notifications for booking confirmations so that I have extra peace of mind that my booking is successful, as external confirmation is the current norm.  
  - FEATURE/TASK: Reservation model:
    - Create model that will contain and save the data in relevant fields for a restaurant booking.

- __User Auth__
  - USER STORY: Account creation / login:
    - As a user I want to be able to sign up for an account/log in to my account so that I can book or manage reservation.
  - USER STORY: Account management:
    - As a user I want to be able to view my account details so that I can confirm and edit my details, or delete my account.
  - FEATURE/TASK: 403 Pages:
    - All pages that require authentication need a 403 Error if unauthorized access is detected.

- __Design__
  - USER STORY: Contact and location info:
    - As a user I want to be able to see the restaurants contact info and location so that I can call them if needed, or see where the restaurant is.
  - USER STORY: Wants to see the menu:
    - As a user I want to be able to view the menu so that I can decide if I like the items sold or not before going.
  - FEATURE/TASK: Style Auth pages:
    - Auth pages need work to fit inputs and layout into the website theme.
  - FEATURE/TASK: 500 page design:
    - Create a custom 500 error page that inherits from base.html.
  - FEATURE/TASK: 404 page design:
    - Create a custom 404 error page that inherits from base.html.
  - FEATURE/TASK: 403 page design:
    - Create a custom 403 error page that inherits from base.html.
  - FEATURE/TASK: Home page design:
    - Home page design, HTML and CSS content.
  - FEATURE/TASK: Booking page design:
    - Booking page design, HTML and CSS content.
  - FEATURE/TASK: Manage booking page design:
    - Manage booking page design, HTML and CSS content.
  - FEATURE/TASK: Detailed reservation view page design:
    - Detailed reservation page design, HTML and CSS content.
  - FEATURE/TASK: Responsivity:
    - All elements must resize based on screen sizes across every template.

- __Capacity__
  - USER STORY - OWNER: Capacity limit
    - As the owner I would like my restaurant to have a capacity limit so that we cannot overbook.
  - USER STORY: Wants to choose a preferred table during booking:
    - As a user I want to see the floor plan so that I know which table I would prefer to book.
  - FEATURE/TASK: Can't double book:
    - Users can't book twice on the same day. Each reservation made by a single user must be on new days.
  - FEATURE/TASK: Table model:
    - As a user I want to see the floor plan so that I know which table I would prefer to book.
  - FEATURE/TASK: Floor plan:
    - Floor plan will give users an understandable overview of where each table number is.

- __Staff Booking Management__
  - USER STORY - STAFF: Wiew all bookings:
    - As a staff member I can view all current bookings in a list view so that I can read their details or perform CRUD operations.
  - USER STORY - STAFF: Cancel bookings:
    - As a staff member I can cancel any bookings from users so that I can manage black listed customers, any potential problems with specific reservations, etc.
  - USER STORY - STAFF: Edit menu items:
    - As a staff member I want to be able to edit items on the menu database so that I can change information about them, f.e. name, ingredients. etc.
  - USER STORY - STAFF: Delete menu items:
    - As a staff member I want to be able to delete items off the menu database so that I can remove them from the menu page if we don't sell it anymore.

- __Menu__
  - USER STORY - STAFF: Add menu items:
    - As a staff member I want to be able to add items to the menu database so that I can add extra items to the database to render on our menu page.
  - USER STORY - STAFF: Add menu items:
    - As a staff member I want to be able to add items to the menu database so that I can add extra items to the database to render on our menu page.
  - FEATURE/TASK: Menu database:
    - The online menu can be turned into a database for easier adjustments by staff when items are added or edited.

- __Documentation__
  - FEATURE/TASK: Floor plan:
    - Floor plan will give users an understandable overview of where each table number is.
  - FEATURE/TASK: Validation:
    - Validate all pages to enforce standards

<br>

### Core Focus
With the limited time for this iteration the focus so far has been to deliver a robust booking system and easy to use interface, as well as lay strong foundations for future implementations and expanded features.  
The core development focus for this iteration was on the customer booking feature and it's related content and dependencies.  
Given a longer iteration the next step would have been a custom user model that builds around the e-mail being the primary identifier and giving users the ability to manage their own account details.  

I feel the goals for the current iteration were met by and large. I've delivered a strong booking feature with robust validation and testing.  

<br>

### Future Focus

- Adjust the cancel functionality so that User canceled reservations are added to a canceled item list for analytics and management purposes.
- Cancelation prompt will include form for cancelation reason, provides information for the restaurant.

- Account registration will use e-mail instead of a seperate username.
- Account managing system for Users to adjust their details.
- All operations around bookings and account management will send e-mails to User's associated e-mail. This will include all CRUD operations by both Staff and their own User account that affected their reservation items.
- Capacity model and table availability tracking

- Menu database models to allow customizable menu items to be displayed.
- Iterate the menu items with Django Template Language.
- Staff account will get a custom interface where they can add, delete and change items.

<br>

For a full overview of all tasks, prioritization and backlog, please look at the [project board](https://github.com/users/jomazzei/projects/4/views/1).

<br>


## Current Key User Story Implementations
[back to content table](#table-of-contents)

<br>

### USER STORY Contact and location info

"As a user I want to be able to see the restaurants contact info and location so that I can call them if needed, or see where the restaurant is."

I chose to combine the contact information and the booking form onto 1 page, as I feel the information is relevant to eachother in a case where the user wants to know what number to dial if they'd like to make a reservation over the phone.

#### Contact Section
![contactpage](/DocAssets/contact-page.png)

#### Contact Footer Information
![contactfooter](/DocAssets/contact-footer.png)

<br>

### USER STORY Account creation and login

"As a user I want to be able to sign up for an account/log in to my account so that I can book or manage reservation."

I used the Django AllAuth package to handle User registration and log in. It's a perfect solution that saves on time otherwise spent making custom models and authorization.
Where ever there's an authorization prompt, customized templates from AllAuth will be rendered and handle the necessary information.

#### Sign Up
![signuppage](/DocAssets/sign-up.png)

#### Log In
![loginpage](/DocAssets/log-in.png)

#### Log Out
![logoutpage](/DocAssets/log-out.png)

<br>

### USER STORY Book a table

"As a user I want to book a table so that I can secure a reservation."

The User can navigate to the booking form in a number of ways. There's a button rendered in the nav bar, a link item in the footer menu and a call to action section on the home page.  
I chose to leave the navigation items for the booking page available to Guests and logged in Users as this page contains 1. contact information for the restaurant, and 2. it encourages Users to go to the page and sign up to use our form.  

For this feature to work it required a custom Reservation model to be made, and the default form validation to be overruled by explicit cleaning parameters to ensure the right values are passed to the database.  
The model holds all relevant information related to booking with a restaurant, including:
  
- Customer's name.
- E-mail address.
- Desired booking date and time, up to an hour before closing time.
- Guest count for the table, with a max table size of 8 people.
- Any special comments or requests.

All information is stored as a Reservation entry into the live database and able to be recalled in necessary functions.  
Additionally, there is a check in place in the booking view that compares the dates of the new entry request against the User's previous entries. If matching, the User is instructed to navigate to that booking and change details or cancel it if they'd like to affect that date in particular.  
On completion and validation of a new booking, the User is redirected straight to the detail view of the newly created item so they can 1. see their details, and 2. know they have successfully created a booking along with the feedback from the toast messages.  

![booknowpage](/DocAssets/booking-fresh.png)
![booknowscrolled](/DocAssets/booking-scrolled.png)

<br>

### USER STORY View own bookings

"As a user I can access my own bookings so that I can edit their details, cancel them, or just view them."  

The User can navigate to this page view the nav bar item for "My bookings" or the footer menu link, both of which are only available in the rendered page when logged in.  
I used the LoginRequired mixin decorator for this class based view so that if a Guest visits the associated link for the list view directly, they will be prompted to log in.  
If they log in, they will be able to see all their own Reservation items if any are available to them. The logic for returning User associated items is in the _get_queryset_ function.
If they do not log in, they cannot enter the page, every time they try they will be met with the log in prompt.  

From the list view, if there are any items available, the User will be able to click on any of the items to see further associated information about that entry.  
The detail view will recall all their entered information for that booking and display it back to the User. From here they will be able to access the Update and Delete functions.  

#### List View
![listviewpage](/DocAssets/list-view.png)

#### Detail View
![detailviewpage](/DocAssets/detail-view.png)

<br>

### USER STORY Edit reservation details

"As a user I want to be able to change specifics about my reservation so that I can reschedule or tweak the guest count to suit my needs."  

The User can navigate to this page from the detailed Reservation view and clicking on the green button at the bottom of the card that says "Edit Reservation".  
When clicked, the User is taken to a prepolutated form, which is a different form in the forms.py file for the sake of different labels, which contains all their current information associated with the item.  

The User can change any of the details they would like to with no restrictions except for date matching.  
Like with creating a new booking, this view compares the requested date with other entries from the same User, excluding itself. If any matches are found, the same error message from the create view will inform the User here.  

If the User instead would like to _not_ commit their changes to the entry, there is a grey button supplied at the bottom of the card that will revert to the detail view and discard their changes.

![updatepage](/DocAssets/update.png)

<br>

### USER STORY Cancel booking

"As a user I want to be able to cancel a booking so that I can change the schedule of my plans / let the restaurant know I won't be showing up."

Like with the Update view, there is a red button supplied at the bottom of the detail view card that says "Cancel Reservation".  
Upon clicking this button, JavaScript will pop up a modal that asks the User for an extra input to protect against accidental cancellation of their booking.
Using bootstrap modals in this way ensures good user experience by providing a non-intrusive confirmation box.

![deletemodal](/DocAssets/delete-modal.png)

<br>

### Toast feedback message

"Users should get informative visual feedback on CRUD operations."

I've supplied the User lots of feedback with toast messages across all CRUD operations.  
I've ensured these boxes are informative and relative to what the User is (attempting) to do.  
In the case of form errors I've gone with the error toast directing the User to the form as the built in Crispy errors are a lot nicer and less obtrusive in displaying errors than it would be to add them all into a toast.

#### Create Booking
![createtoast](/DocAssets/book-toast.png)

#### Update Booking
![updatetoast](/DocAssets/update-toast.png)

#### Cancel Booking
![canceltoast](/DocAssets/cancel-toast.png)

#### Error
![errortoast](/DocAssets/error-toast.png)

<br>


## Validation and Testing
[back to content table](#table-of-contents)

<br>

This project is currently undergoing the following validations and performance tests, and are updated according to progress.
### Validation
- __HTML__
  - [The W3C Markup Validator](https://validator.w3.org/#validate_by_input)
    - Sign up page has failed validation. 4 errors were found:
      - End tag p implied, but there were open elements.
      -  Unclosed element span.
      -  Stray end tag span.
      -  No p element in scope but a p end tag seen.
    - These errors seem to stem from the current version of Django AllAuth. A future update will see a potential downgrade to a previous error-free version and an overhaul to the auth pages styling and content.
    - All other pages have passed validation
- __CSS__
  - [The W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    - Line 205 has failed validation, "	Property shape-outside doesn't exist : circle(45%)". It's a false positive, as the value does exist and works, including having [documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/shape-outside), but is considered experimental/not generally supported so a future update to the project will include an alternative option to wrap the text.
    - All other values have passed validation.
- __Python Linter__
  - [CI Python Linter](https://pep8ci.herokuapp.com/)
    - The settings.py file has 4 line too long errors, line 131, 134, 137, 140. These are default lines that Django generates during the set up process and as such were not touched.
    - All other files have passed validation and were formatted to PEP8 standards.

<br>

### Performance and Contrast Tests
- __Performance__
  - [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview)
    - Computer: All pages were tested for performance, averaging 97.88 total. Only the Home page dipped below 100 performance at 82, due to large content having to be loaded at once.
    - Mobile: All pages were tested for performance, averaging 93.75 total. Again, the Home page dipped significantly from 97 to 72, due to large content having to be loaded.
    - Across the board the website scored well on accessability, ranging from 90-100.
    - Website SEO scored weaker at 82 across the board, main issue being missing meta information.

- __Contrast__
  - [WCAG](https://chromewebstore.google.com/detail/plnahcmalebffmaghcpcmpaciebdhgdf)
    - Currently undergoing testing - to be updated.

<br>

### Testing table

<div align="center">

| Test Description  | Expected Result | Actual Result | Pass / Fail |
| ------------- | ------------- | ------------- | ------------- |
| Home page | Home is the default page shown. Can be navigated to from anywhere using the nav tab link or footer link | Home is the default page shown. Can be navigated to from anywhere using the nav tab link | __Pass__ |
| Menu page | Menu page is accessible to all (Guest) Users by clicking the nav tab link or footer link | Menu page is accessible to all (Guest) Users by clicking the nav tab link or footer link | __Pass__ |
| Sign up feature | Guest Users can enter information on sign up page. On successful registration the user account is stored and accessible via admin panel and log in page. | Users can sign up and their information is stored for use in authentication  | __Pass__  | 
| Log in feature | Users can enter the same information from sign up on the log in page, enabling autherized pages and features | Users can log in and gain authorization to specific features | __Pass__ | 
| Log out feature | Users can log out from the logout page and lose access to autherized features | A logged in User can log themselves out, disabling autherized features | __Pass__ |
| Booking page | (Guest) Users can open the book now page and see all relevant restaurant information, a Guest User will be presented with a prompt to log in or sign up instead of a form | Anyone can access the book now page, with unauthorized users being presented with a log in / sign up prompt | __Pass__ | 
| Booking form validation | Users cannot bypass the form by tweaking values using dev tools and removing required tags or changing data types. All values validated in the backend | Users cannot bypass the form by tweaking values using dev tools and removing required tags or changing data types. All values validated in the backend | __Pass__ |
| My bookings page | Logged in Users can click on the "my bookings" nav tab and see all their bookings if any available, they will only be able to see their own bookings. A logged out Guest User will be prompted to log in and cannot view the page until they do so | Logged in Users can click on the "my bookings" nav tab and see all their bookings if any available, they will only be able to see their own bookings. A logged out Guest User will be prompted to log in and cannot view the page until they do so | __Pass__ |
| Reservation details page | Logged in User can see the details of their reservation by clicking on one of their list items. Users can access the deletion and update functions from here. Logged out Guest Users are prompted to log in and cannot view the page until they do so | Logged in user can see the details of their reservation by clicking on one of their list items. Users can access the deletion and update functions from here. Logged out Guest Users are prompted to log in and cannot view the page until they do so | __Pass__ |
| Reservation details authorization | Logged in User can access all their details. If a non-logged in Guest User navigates to a reservation URL they will be prompted to log in. If an account that does not own a reservation navigates to the link they will be shown a 403 error page instead of the reservation details | Logged in User can access all their details. If a non-logged in Guest User navigates to a reservation URL they will be prompted to log in. If an account that does not own a reservation navigates to the link they will be shown a 403 error page instead of the reservation details | __Pass__ |
| Reservation update page | Logged in User can navigate to the update view by clicking the update details button at the bottom of the detailed view. Here they can change any of their relevant reservation details. Logged out Guest Users prompted to log in | Logged in User can navigate to the update view by clicking the update details button at the bottom of the detailed view. Here they can change any of their relevant reservation details. Logged out Guest Users prompted to log in | __Pass__ |
| Reservation update authorization | Only related User can see and change the details of the update view. Any unrelated logged in User accounts will be shown a 403 error instead of being able to access the URL | Only related User can see and change the details of the update view. Any unrelated logged in User accounts will be shown a 403 error instead of being able to access the URL | __Pass__ |
| Reservation delete function | Logged in User can delete their reservation by clicking the button at the bottom of the detailed view page. The button will prompt a bootstrap modal for confirmation, the User can click confirm cancellation or back out in this pop up | Logged in User can delete their reservation by clicking the button at the bottom of the detailed view page. The button will prompt a bootstrap modal for confirmation, the User can click confirm cancellation or back out in this pop up | __Pass__  |
| Reservation delete authorization | Only related User can delete a specific reservation through the delete function. Any unrelated User accounts would be shown a 403 error if they attempt to link directly to the delete function for that page | Only related User can delete a specific reservation through the delete function. Any unrelated User accounts would be shown a 403 error if they attempt to link directly to the delete function for that page | __Pass__ |
| Reservations cannot be booked on the same day by 1 User | A single User account cannot have multiple bookings on the same day. If attempting to book multiple bookings for the same day they will be shown a toast error message describing a recommended course of action. If attempting to update an existing booking to the same date as another existing booking, they will be shown a toast error message describing a recommended course of action | A single User account cannot have multiple bookings on the same day. If attempting to book multiple bookings for the same day they will be shown a toast error message describing a recommended course of action. If attempting to update an existing booking to the same date as another existing booking, they will be shown a toast error message describing a recommended course of action | __Pass__ |
| E-mail and phone number links | Contact links will automatically open in default provider when clicked | Contact links will automatically open in default provider when clicked. Behavior matches in both booking page and footer links | __Pass__ |

</div>

<br>

### Test Module and Debugging

I only encountered relatively minor bugs throughout the creation of the project up to this stage, any noteable bugs that halted development for any measure of time were tracked on the [project board](https://github.com/users/jomazzei/projects/3/views/1).  

The only real noteable bug I got hung up on was [Issue #20](https://github.com/jomazzei/charredchops/issues/20).  
When a User enters information and submits the form, it would throw an error. Debugging error messages list wouldn't show up in the template, just that the form did not save.

To start, I searched for potential problems on Google but nothing matched my issue. I then ran my code through ChatGPT to see if I missed anything but it could not spot any errors.  
After those two initial high level options I created a tests_forms.py file and a test case with hardcoded values for my form fields to see if there were problems in my form. This was to rule out any errors on the form validation, even though initially I never got any form errors displayed in print statements or template iterations.  

The form handled values correctly and my tests passed. Not being able to find my issue this way, I added print statements to each step of my form handling process. The form would get to POST request, couldn't save, but also wouldn't come back with any errors.  
I compared my form handling code to others' on stack overflow again and this time noticed that I was missing the argument _request.POST_ in my POST instance of the form.  

While the solution was really simple in the end, I include this section as it displayed my debugging process where it was necessary in my project.  

  - Currently the full view of all tracked and fixed bugs can be found on the [project board](https://github.com/users/jomazzei/projects/3/views/1)

<br>


## Forking
To set up your own fork from this repo, these are the general steps and things to take into account:  

To start the fork, go to the top of this repo and click on the fork dropdown, follow its process.  
Install the requirements using `pip install -r requirements.txt`.  

Create a `env.py` file and write out the environment variables for:  

  - `DEBUG`, any value.
  - `SECRET_KEY`, write out your own combination of characters.
  - `DB_URL`, link to your own database. I have used ElephantSQL's free postgres database for my production.  

Your lines should look similar to this:  
`os.environ.setdefault("DEBUG", "1")`  
`os.environ.setdefault("SECRET_KEY", "******")`  
`os.environ.setdefault("DB_URL", "postgres://")`  

In `settings.py` make sure `DEBUG` near the top of the file reads:  
`DEBUG = 'DEBUG' in os.environ`  
This line automatically handles whether `DEBUG` should be set to True or False depending on the availability of the `env.py` file in your workspace vs. deployment.  
Though not necessary, for safety and good practice put `DEBUG` to False instead of the `DEBUG = 'DEBUG' in os.environ` line on your deployment branch or push.  

If deploying on Heroku, in your app settings click reveal config vars and add `SECRET_KEY` and `DB_URL`.  
`SECRET_KEY` does not have to match the same as your `env.py`, but `DB_URL` should be the same if you have been accessing that database during local development.  

This file is not included in the repo as it contains sensitive data in links and keys that require hiding from public usage.  

<br>


## Credits
[back to content table](#table-of-contents)
<br>
<br>

### Images
![logo](/DocAssets/cc-logo-bg.png)
- Created logo on Krita.

<br>

![Hero](static/media/steak-img1.png)
- Hero steak image on home page generated by [Pixlr AI generator](https://pixlr.com/image-generator/)

<br>

![Chef](/static/media/chef-grilling.png)
- Chef image in who we are section generated by [Pixlr AI generator](https://pixlr.com/image-generator/)

<br>

##### _Disclaimer_
  _<p>Images generated by AI has the posibility to be based on online creators' works</p>_
  _<p>For the use of the included images, AI training content is presumed to have been fairly compensated</p>_

<br>

### Content and Code
- Design inspirations from [Miller & Carter steakhouse](https://www.millerandcarter.co.uk/).
- Basic outline for header, footer and hero image section adapted from [Love Running walkthrough project](https://github.com/jomazzei/love-running), originally created by [Code Institute](https://codeinstitute.net/?_gl=1*xh7bh0*_up*MQ..&gclid=CjwKCAjwkuqvBhAQEiwA65XxQA_KVRG0RaWOXmBe9aqfp9kJ_Vw14KkL0WQhpPMGA4STT5MNmkBC2hoC-aUQAvD_BwE).
- Baseline HTML template for AllAuth taken from [Django blog walkthrough project](https://github.com/jomazzei/django-blog), originally created by [Code Institute](https://codeinstitute.net/?_gl=1*xh7bh0*_up*MQ..&gclid=CjwKCAjwkuqvBhAQEiwA65XxQA_KVRG0RaWOXmBe9aqfp9kJ_Vw14KkL0WQhpPMGA4STT5MNmkBC2hoC-aUQAvD_BwE).
- Baseline code for similar functions, such as List view and Form submission view adapted from [Django blog walkthrough project](https://github.com/jomazzei/django-blog), originally created by [Code Institute](https://codeinstitute.net/?_gl=1*xh7bh0*_up*MQ..&gclid=CjwKCAjwkuqvBhAQEiwA65XxQA_KVRG0RaWOXmBe9aqfp9kJ_Vw14KkL0WQhpPMGA4STT5MNmkBC2hoC-aUQAvD_BwE).
- Delete modal prompt adapted from the hackathon project [Campus Connect](https://github.com/jomazzei/campus-connect).
- Who we are section text generated by [ChatGPT](https://chat.openai.com/).
- ReadMe structure templated from the hackathon project [Campus Connect](https://github.com/jomazzei/campus-connect), from which the ReadMe was originally based off of hackathon project [Belgian Bakes](https://github.com/Tariq-845/belgian-bakes).
- ReadMe table from [mooict](https://www.mooict.com/how-to-test-software-using-test-table/).
- Referred to various sources (not all inclusive) for fixes and implementations for features I wasn't knowledgeable on:
  - Django docs
  - Bootstrap docs
  - Stackoverflow
  - ChatGPT
  - YouTube
  - W3 Schools
  - Geeks for Geeks

<br>

#### Note on the use of ChatGPT for coding related queries
I ensured that I used ChatGPT only as an assisting tool throughout this project.
Most use-cases were not finding the right answers on stackoverflow to aid in writing out my functions or needing a more specific question answered.
These answers were often items in the Django docs or other tools and packages that I didn't know existed - such as built-in parameters like "context_object_name" and "validators", or "datetime" and "string" modules.

In more specific code block cases, my questions centered around debugging and making sure I was on the right track for the sake of time.
One such instance is writing a for loop for every form error from the view rather than the template, and displaying them in a single toast message. I couldn't get it to work within a single toast message and went back to iterating from the template.

<hr>
<br>

#### _A thank you_
I wanted to extend a heartfelt thanks to..  
David, our group's facilitator, for his support to us throughout the bootcamp.  
Kevin and Martin, our SME and Coding Coaches, for their wealth of knowledge and insight.  
Daisy, my mentor, for helping me during the past 2 weeks in reviewing and honing in on my project.  
The entire bootcamp group, for sharing their thoughts and projects during this whole course.  
Finally all together for being great people and it's been fun getting to know everyone.  

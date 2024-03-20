<p align="center"><img src="/DocAssets/cc-logo-bg.png"></p>
<hr>

<h1 align="center">Charred Chops</h1>

[View live deployment here!](https://jomazzei-charred-chops-161a869d9d8b.herokuapp.com/)

<p>This website project is for a hypothetical steakhouse, Charred Chops, with the main goal of offering a user friendly manner to book and manage a reservation with the restaurant.</p>
<p>In future the features of the application will scale beyond just user reservation, also offering the staff a way to manage the displayed menu and manage all customer bookings</p>

<hr>

<br>


#### Table of Contents:

* [Project Methodology and Tech Stack](#project-methodology-and-tech-stack)
* [Wireframes](#wireframes)
  * [Home page](#home-page)
  * [booking page](#booking-page) 
* [User Stories and Features](#user-stories-and-features)
* [Testing](#testing)
* [Credits](#credits)

<br>  


## Project Methodology and Tech Stack
[back to content table](#table-of-contents)
<br>
<br>

- __Ideation & Project Management__


- __Development__


<br>


## Wireframes
[back to content table](#table-of-contents)
<br>
<br>

### Home Page
![home](/DocAssets/home-fresh-view.png)

<br>

### Booking Page
![bookingpage](/DocAssets/booking-logged-in.png)

<br>

<br>

## User Stories and Features

### Core Focus
Core stories and features revolve around what the main purpose of the website is.   
These include:
<ul>
<li></li>
</ul>

### Features Left to Implement
The main features left to implement are currently:
- 

For a full overview of all user stories and features, please look at the [project board](https://github.com/users/jomazzei/projects/4/views/1).

<br>


## Testing 
[back to content table](#table-of-contents)
<br>
<br>

This project is currently undergoing the following validations and performance tests, and are updated according to progress
### Validation
- __HTML__
  - [The W3C Markup Validator](https://validator.w3.org/#validate_by_input)
- __CSS__
  - [The W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- __Python Linter__
  - [CI Python Linter](https://pep8ci.herokuapp.com/)

### Performance & Contrast Tests
- __Performance__
  - [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview)
- __Contrast__
  - [WCAG](https://chromewebstore.google.com/detail/plnahcmalebffmaghcpcmpaciebdhgdf)

### Debugging & Test Module
-__Some of the key bugs will be listed here and how they were dealt with__
  - Currently the full view of all tracked and fixed bugs can be found on the [project board](https://github.com/users/jomazzei/projects/3/views/1)

<br>


# Credits
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
- Design inspirationas from [Miller & Carter steakhouse](https://www.millerandcarter.co.uk/).
- Baseline HTML template for AllAuth taken from [Django blog walkthrough project](https://github.com/jomazzei/django-blog), originally created by [Code Institute](https://codeinstitute.net/?_gl=1*xh7bh0*_up*MQ..&gclid=CjwKCAjwkuqvBhAQEiwA65XxQA_KVRG0RaWOXmBe9aqfp9kJ_Vw14KkL0WQhpPMGA4STT5MNmkBC2hoC-aUQAvD_BwE).
- Baseline code for similar functions, such as List view and Form submission view adapted from [Django blog walkthrough project](https://github.com/jomazzei/django-blog), originally created by [Code Institute](https://codeinstitute.net/?_gl=1*xh7bh0*_up*MQ..&gclid=CjwKCAjwkuqvBhAQEiwA65XxQA_KVRG0RaWOXmBe9aqfp9kJ_Vw14KkL0WQhpPMGA4STT5MNmkBC2hoC-aUQAvD_BwE).
- ReadMe structure templated from the hackathon project [Campus Connect](https://github.com/jomazzei/campus-connect), from which the ReadMe was originally based off of hackathon project [Belgian Bakes](https://github.com/Tariq-845/belgian-bakes).
- Referred to various sources (not all inclusive) for fixes and implementations for features I wasn't knowledgeable on:
  - Django docs
  - Bootstrap docs
  - Stackoverflow
  - ChatGPT
  - YouTube
  - W3 Schools
  - Geeks for Geeks

<br>

#### Note on the use of ChatGPT for coding related queries:
I ensured that I used ChatGPT only as an assisting tool throughout this project.
Most use-cases were not finding the right answers on stackoverflow to aid in writing out my functions or needing a more specific question answered.
These answers were often items in the Django docs or other tools and packages that I didn't know existed - such as built-in parameters like "context_object_name" and "validators", or "datetime" and "string" modules.

In more specific code block cases, my questions centered around debugging and making sure I was on the right track for the sake of time.
One such instance is writing a for loop for every form error from the view rather than the template, and displaying them in a single toast message. I couldn't get it to work within a single toast message and went back to iterating from the template
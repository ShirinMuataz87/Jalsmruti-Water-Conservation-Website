# API Endpoints

## Home API Endpoints

### GET /
Retrieve the home page of the site.

**Response:**
- 200 OK: Returns the home page content.

### GET /about/
Retrieve the about page of the site.

**Response:**
- 200 OK: Returns the about page content.

### POST /contact_form/
Submit the contact form with rate throttling and reCAPTCHA validation.

**Request:**
- Form Data: Contact form fields including reCAPTCHA response.

**Response:**
- 302 Found: Redirects to the original page with the footer anchor or to the home page with the footer anchor.
- 400 Bad Request: Returns an error message if the form is invalid or reCAPTCHA validation fails.
- 429 Too Many Requests: Returns an error message if the rate limit is exceeded.

## Initiative API Endpoints

### GET /initiative/
Retrieve the initiative section index page.

**Response:**
- 200 OK: Returns the initiative section index page content.

### GET /initiative/<int:pk>/<slug:slug>/
Retrieve a specific initiative post based on the primary key and slug.

**Response:**
- 200 OK: Returns the initiative post details.
- 404 Not Found: If the initiative post does not exist or the slug does not match.

## Insight API Endpoints

### GET /insight/
Retrieve the insight section index page.

**Response:**
- 200 OK: Returns the insight section index page content.

### GET /insight/<int:pk>/<slug:slug>/
Retrieve a specific insight post based on the primary key and slug.

**Response:**
- 200 OK: Returns the insight post details.
- 404 Not Found: If the insight post does not exist or the slug does not match.

## Event API Endpoints

### GET /event/
Retrieve the event section index page.

**Response:**
- 200 OK: Returns the event section index page content.

### GET /event/<int:pk>/<slug:slug>/
Retrieve a specific event post based on the primary key and slug.

**Response:**
- 200 OK: Returns the event post details.
- 404 Not Found: If the event post does not exist or the slug does not match.


## Team API Endpoints

### GET /team/
Retrieve the team section index page.

**Response:**
- 200 OK: Returns the team section index page content.

### GET /team/<int:pk>/<slug:slug>/
Retrieve a specific team post based on the primary key and slug.

**Response:**
- 200 OK: Returns the team post details.
- 404 Not Found: If the team post does not exist or the slug does not match.

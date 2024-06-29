# Database Design

## Tables and Relationships

### EventSection Table

- **name**: `CharField` - The name of the section.
- **title**: `CharField` - The title of the section.
- **heading**: `CharField` - The heading of the section.
- **description**: `RichTextField` - A detailed description of the section.
- **keywords**: `CharField` - Keywords associated with the section for SEO purposes.
- **image**: `ImageField` - An image associated with the section.

### EventPost Table

- **title**: `CharField` - The title of the post (unique).
- **url_slug**: `AutoSlugField` - A URL-friendly slug generated from the title (unique).
- **image**: `ImageField` - An image associated with the post.
- **description**: `CharField` - A short description of the post.
- **keywords**: `CharField` - Keywords associated with the post for SEO purposes.
- **body**: `RichTextField` - The main content of the post.
- **type**: `CharField` - The type of the post.
- **category**: `CharField` - The category of the post.
- **created_on**: `DateField` - The date the post was created.
- **start_time**: `TimeField` - The start time of the event.
- **end_time**: `TimeField` - The end time of the event.
- **mode**: `CharField` - The mode of the event (e.g., online, offline).
- **last_modified**: `DateTimeField` - The date and time when the post was last modified.

### HomeSection Table

- **name**: `CharField` - The name of the section.
- **title**: `CharField` - The title of the section.
- **heading**: `CharField` - The heading of the section.
- **description**: `RichTextField` - A detailed description of the section.
- **keywords**: `CharField` - Keywords associated with the section for SEO purposes.
- **image**: `ImageField` - An image associated with the section.
- **challenge**: `RichTextField` - The challenge description for the home section.
- **approach**: `RichTextField` - The approach description for the home section.

### Fact Table

- **facts**: `CharField` - The fact description.
- **percentage**: `IntegerField` - The percentage value of the fact.

### SocialMedia Table

- **name**: `CharField` - The name of the social media platform.
- **url**: `TextField` - The URL of the social media profile.

### Message Table

- **email**: `EmailField` - The email address of the sender.
- **name**: `CharField` - The name of the sender.
- **query**: `CharField` - The message/query from the sender.
- **receive_newsletter**: `BooleanField` - Whether the sender wants to receive the newsletter.

### AboutPage Table

- **name**: `CharField` - The name of the section.
- **title**: `CharField` - The title of the section.
- **heading**: `CharField` - The heading of the section.
- **description**: `RichTextField` - A detailed description of the section.
- **keywords**: `CharField` - Keywords associated with the section for SEO purposes.
- **image**: `ImageField` - An image associated with the section.
- **challenges**: `RichTextField` - The challenges description for the about page.
- **vision_mission**: `RichTextField` - The vision and mission description for the about page.
- **services**: `RichTextField` - The services description for the about page.
- **team**: `RichTextField` - The team description for the about page.
- **team_image**: `ImageField` - The team image for the about page.

### Image Table

- **name**: `CharField` - The name of the image.
- **image**: `ImageField` - The image file.

### InitiativeSection Table

- **name**: `CharField` - The name of the section.
- **title**: `CharField` - The title of the section.
- **heading**: `CharField` - The heading of the section.
- **description**: `RichTextField` - A detailed description of the section.
- **keywords**: `CharField` - Keywords associated with the section for SEO purposes.
- **image**: `ImageField` - An image associated with the section.

### InitiativePost Table

- **title**: `CharField` - The title of the post (unique).
- **url_slug**: `AutoSlugField` - A URL-friendly slug generated from the title (unique).
- **image**: `ImageField` - An image associated with the post.
- **description**: `CharField` - A short description of the post.
- **keywords**: `CharField` - Keywords associated with the post for SEO purposes.
- **body**: `RichTextField` - The main content of the post.
- **long_description**: `CharField` - A longer description of the post, optional.
- **button**: `CharField` - Text for an associated button, optional.
- **button_url**: `CharField` - URL for the associated button, optional.
- **quote**: `CharField` - A relevant quote for the post, optional.
- **region**: `CharField` - Geographic region related to the post, optional.
- **visit_button**: `CharField` - Text for a visit button, optional.
- **created_on**: `DateTimeField` - The date and time the post was created.
- **last_modified**: `DateTimeField` - The date and time when the post was last modified.

### InsightSection Table

- **name**: `CharField` - The name of the section.
- **title**: `CharField` - The title of the section.
- **heading**: `CharField` - The heading of the section.
- **description**: `RichTextField` - A detailed description of the section.
- **keywords**: `CharField` - Keywords associated with the section for SEO purposes.
- **image**: `ImageField` - An image associated with the section.

### InsightPost Table

- **title**: `CharField` - The title of the post (unique).
- **url_slug**: `AutoSlugField` - A URL-friendly slug generated from the title (unique).
- **image**: `ImageField` - An image associated with the post.
- **description**: `CharField` - A short description of the post.
- **keywords**: `CharField` - Keywords associated with the post for SEO purposes.
- **body**: `RichTextField` - The main content of the post.
- **author**: `CharField` - The author of the post.
- **category**: `CharField` - The category of the post.
- **topic**: `CharField` - The topic of the post.
- **region**: `CharField` - The region related to the post (optional).
- **created_on**: `DateTimeField` - The date and time the post was created.
- **last_modified**: `DateTimeField` - The date and time when the post was last modified.

### TeamSection Table

- **name**: `CharField` - The name of the section.
- **title**: `CharField` - The title of the section.
- **heading**: `CharField` - The heading of the section.
- **description**: `RichTextField` - A detailed description of the section.
- **keywords**: `CharField` - Keywords associated with the section for SEO purposes.
- **image**: `ImageField` - An image associated with the section.

### TeamPost Table

- **title**: `CharField` - The title of the post (unique).
- **url_slug**: `AutoSlugField` - A URL-friendly slug generated from the title (unique).
- **image**: `ImageField` - An image associated with the post.
- **description**: `CharField` - A short description of the post.
- **keywords**: `CharField` - Keywords associated with the post for SEO purposes.
- **body**: `RichTextField` - The main content of the post.
- **position**: `CharField` - The position of the team member.
- **linkedin**: `CharField` - The LinkedIn profile URL of the team member.
- **language**: `CharField` - The language(s) spoken by the team member.
- **last_modified**: `DateTimeField` - The date and time when the post was last modified.

### Relationships

- **EventSection**: Inherits from `BaseSection`. No direct relationships with other tables.
- **EventPost**: Inherits from `BasePost`. No direct relationships with other tables.
- **HomeSection**: Inherits from `BaseSection`. No direct relationships with other tables.
- **Fact**: No direct relationships with other tables.
- **SocialMedia**: No direct relationships with other tables.
- **Message**: No direct relationships with other tables.
- **AboutPage**: Inherits from `BaseSection`. No direct relationships with other tables.
- **Image**: No direct relationships with other tables.
- **InitiativeSection**: Inherits from `BaseSection`. No direct relationships with other tables.
- **InitiativePost**: No direct relationships with other tables.
- **InsightSection**: No direct relationships with other tables.
- **InsightPost**: No direct relationships with other tables.
- **TeamSection**: Inherits from `BaseSection`. No direct relationships with other tables.
- **TeamPost**: No direct relationships with other tables.
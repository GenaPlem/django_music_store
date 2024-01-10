# Testing

This document provides an overview of the testing strategies applied throughout the development of the M-TUNE e-commerce store. It includes various types of testing to ensure functionality, compatibility, usability, and responsiveness of the application.

## Code Validation

### HTML

I've used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page             | Screenshot                                                                       | Notes           |
|------------------|----------------------------------------------------------------------------------|-----------------|
| Home             | ![screenshot](documentation/images/testing/html_validation/home.png)             | Pass: No Errors |
| Products         | ![screenshot](documentation/images/testing/html_validation/products.png)         | Pass: No Errors |
| Product Detail   | ![screenshot](documentation/images/testing/html_validation/product_detail.png)   | Pass: No Errors |
| Contact          | ![screenshot](documentation/images/testing/html_validation/contact.png)          | Pass: No Errors |
| Wishlist         | ![screenshot](documentation/images/testing/html_validation/wishlist.png)         | Pass: No Errors |
| Sign Up          | ![screenshot](documentation/images/testing/html_validation/register.png)         | Pass: No Errors |
| Sign In          | ![screenshot](documentation/images/testing/html_validation/login.png)            | Pass: No Errors |
| Change Password  | ![screenshot](documentation/images/testing/html_validation/pass_change.png)      | Pass: No Errors |
| Reset Password   | ![screenshot](documentation/images/testing/html_validation/pass_reset.png)       | Pass: No Errors |
| Search           | ![screenshot](documentation/images/testing/html_validation/search.png)           | Pass: No Errors |
| Log Out          | ![screenshot](documentation/images/testing/html_validation/logout.png)           | Pass: No Errors |
| Bag              | ![screenshot](documentation/images/testing/html_validation/bag.png)              | Pass: No Errors |
| Checkout         | ![screenshot](documentation/images/testing/html_validation/checkout.png)         | Pass: No Errors |
| Checkout Success | ![screenshot](documentation/images/testing/html_validation/checkout_success.png) | Pass: No Errors |
| Profile          | ![screenshot](documentation/images/testing/html_validation/profile.png)          | Pass: No Errors |
| Orders           | ![screenshot](documentation/images/testing/html_validation/orders.png)           | Pass: No Errors |
| Add Product      | ![screenshot](documentation/images/testing/html_validation/add_product.png)      | Pass: No Errors |
| Edit Product     | ![screenshot](documentation/images/testing/html_validation/edit_product.png)     | Pass: No Errors |
| Delete Product   | ![screenshot](documentation/images/testing/html_validation/delete_product.png)   | Pass: No Errors |

### CSS

#### Current Approach

For the M-TUNE e-commerce platform, a decision was made to streamline the styling process by utilizing Bootstrap's comprehensive library alongside a singular, general-purpose custom CSS file. This approach was taken to maintain a consistent look and feel across the application while also leveraging the responsive and utility-first classes provided by Bootstrap. This ensures that the styles are scalable and easily managed.

#### Future Plans

As the project evolves and the feature set expands, the plan is to modularize the CSS by introducing separate stylesheets for each distinct Django app within the project. This will promote better maintainability and make it easier to manage styles that are specific to certain components or sections of the application. Transitioning to a more granular stylesheet structure will be in alignment with the growing complexity and the need for more specialized styling.

![screenshot](documentation/images/testing/css_validation/css.png)
No errors in styles, there is only few warnings about loader.

### JavaScript

I've used [JShint Validator](https://jshint.com) to validate all of my JS files.

| File                                | Screenshot                                                              | Notes                                       |
|-------------------------------------|-------------------------------------------------------------------------|---------------------------------------------|
| alerts.js                           | ![screenshot](documentation/images/testing/js_validation/alert.png)     | Pass: No Errors                             |
| search_bag.js                       | ![screenshot](documentation/images/testing/js_validation/searchbar.png) | Pass: No Errors                             |
| bag_item_quantity.js                | ![screenshot](documentation/images/testing/js_validation/item_qty.png)  | Pass: No Errors                             |
| stripe_elements.js                  | ![screenshot](documentation/images/testing/js_validation/stripe.png)    | Pass: No Errors (Undefined Stripe variable) |

### Python Code Style and Syntax Testing with Flake8

**Using Flake8**

flake8 is a command-line utility that we used for checking Python code against coding style (PEP 8), programming errors, and code complexity. It's an essential tool in maintaining high-quality, readable, and maintainable code.

Installation and Execution

To use flake8, it needs to be installed via pip <br>`pip3 install flake8`<br>
Once installed, you can run it on your project by simply executing:
`flake8`

This command scans the project's Python files, excluding any paths configured in the .flake8 configuration file.

#### Key Findings and Actions

- **Unused Imports**: `flake8` identified a few unused imports across various files. These were promptly removed to clean up the code.

    ![screenshot](documentation/images/testing/python_validation/unused_imports.png)

- **Line Length Issues**: A common issue found was `line too long (88 > 79 characters)`. To address this, we refactored the code to adhere to the recommended line length of 79 characters. This involved breaking longer lines into shorter, more readable segments.

    ![screenshot](documentation/images/testing/python_validation/long_line.png)

- **No Remaining Errors**: After addressing the above issues, flake8 reported no further errors, indicating improved code health.

    ![screenshot](documentation/images/testing/python_validation/result.png)

#### Why Flake8?

I chose flake8 over other tools for several reasons:

- **Comprehensive Checks**: `flake8` not only checks for style violations but also scans for potential errors in the code like unused variables or imports.

- **Configurability**: It allows us to configure our preferences, like excluding certain files or directories and setting a maximum line length.

- **Integration Ease**: `flake8` is easy to integrate into existing workflows and can be run as part of continuous integration (CI) processes.

- **Community Standard**: It is widely used in the Python community, making it a reliable choice for Python projects.

#### Conclusion

By integrating `flake8` into development process, I have enhanced the readability and maintainability of my code. It has been instrumental in identifying and correcting style inconsistencies and simple errors, contributing to the overall quality of the project.

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Notes             |
|---------|-------------------|
| Chrome  | Works as expected |
| Firefox | Works as expected |
| Edge    | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device            | Notes             |
|-------------------|-------------------|
| Mobile (DevTools) | Works as expected |
| Tablet (DevTools) | Works as expected |
| Laptop            | Works as expected |
| Desktop           | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

During the development process, I conducted Lighthouse audits to evaluate the performance, accessibility, best practices, and SEO of the website. These audits are crucial for understanding how well the site performs on various metrics and for identifying areas for improvement.

### Key Findings:

- **Bootstrap CDN**: The use of Bootstrap's CDN for styles and scripts contributed to warnings about resource loading. While CDNs offer advantages in terms of speed and efficiency, they can sometimes impact performance scores in Lighthouse audits. Considering the project's tight deadline, utilizing the CDN was a necessary compromise to expedite development.

- **Image Optimization**: The current version of the site uses images that are not fully optimized, which has impacted the performance score. Image optimization is a known area for improvement. Due to the project's time constraints, in-depth optimization was not feasible within the given timeline. However, this is a priority for future updates to enhance site speed and performance.

- **CSS and JavaScript Minimization**: The site currently does not employ extensive minimization of CSS and JavaScript files. While this is an acknowledged best practice for improving load times and overall performance, the current focus has been on functionality and feature completion within the project's deadline. Future iterations of the site will include a focus on minimizing these assets for better performance. 

| Page             | Size    | Screenshot                                                                         | Notes               |
|------------------|---------|------------------------------------------------------------------------------------|---------------------|
| Home             | Desktop | ![screenshot](documentation/images/testing/lighthouse/home.png)                    | Some minor warnings |
| Home             | Mobile  | ![screenshot](documentation/images/testing/lighthouse/home_mobile.png)             | Some minor warnings |
| Products         | Desktop | ![screenshot](documentation/images/testing/lighthouse/products.png)                | Some minor warnings |
| Products         | Mobile  | ![screenshot](documentation/images/testing/lighthouse/products_mobile.png)         | Some minor warnings |
| Product Detail   | Desktop | ![screenshot](documentation/images/testing/lighthouse/product_detail.png)          | No major warnings   |
| Product Detail   | Mobile  | ![screenshot](documentation/images/testing/lighthouse/product_detail_mobile.png)   | No major warnings   |
| Contact          | Desktop | ![screenshot](documentation/images/testing/lighthouse/contact.png)                 | No major warnings   |
| Contact          | Mobile  | ![screenshot](documentation/images/testing/lighthouse/contact_mobile.png)          | No major warnings   |
| Wishlist         | Desktop | ![screenshot](documentation/images/testing/lighthouse/wishlist.png)                | No major warnings   |
| Wishlist         | Mobile  | ![screenshot](documentation/images/testing/lighthouse/wishlist_mobile.png)         | Some minor warnings |
| Sign Up          | Desktop | ![screenshot](documentation/images/testing/lighthouse/register.png)                | No major warnings   |
| Sign Up          | Mobile  | ![screenshot](documentation/images/testing/lighthouse/register_mobile.png)         | Some minor warnings |
| Sign In          | Desktop | ![screenshot](documentation/images/testing/lighthouse/login.png)                   | No major warnings   |
| Sign In          | Mobile  | ![screenshot](documentation/images/testing/lighthouse/login_mobile.png)            | Some minor warnings |
| Password Change  | Desktop | ![screenshot](documentation/images/testing/lighthouse/change_pass.png)             | No major warnings   |
| Password Change  | Mobile  | ![screenshot](documentation/images/testing/lighthouse/change_pass_mobile.png)      | Some minor warnings |
| Password Reset   | Desktop | ![screenshot](documentation/images/testing/lighthouse/pass_reset.png)              | No major warnings   |
| Password Reset   | Mobile  | ![screenshot](documentation/images/testing/lighthouse/pass_reset_mobile.png)       | No major warnings   |
| Search           | Desktop | ![screenshot](documentation/images/testing/lighthouse/search.png)                  | No major warnings   |
| Search           | Mobile  | ![screenshot](documentation/images/testing/lighthouse/search_mobile.png)           | No major warnings   |
| Log Out          | Desktop | ![screenshot](documentation/images/testing/lighthouse/logout.png)                  | No major warnings   |
| Log Out          | Mobile  | ![screenshot](documentation/images/testing/lighthouse/logout_mobile.png)           | Some minor warnings |
| Bag              | Desktop | ![screenshot](documentation/images/testing/lighthouse/bag.png)                     | No major warnings   |
| Bag              | Mobile  | ![screenshot](documentation/images/testing/lighthouse/bag_mobile.png)              | Some minor warnings |
| Checkout         | Desktop | ![screenshot](documentation/images/testing/lighthouse/checkout.png)                | No major warnings   |
| Checkout         | Mobile  | ![screenshot](documentation/images/testing/lighthouse/checkout_mobile.png)         | Some minor warnings |
| Checkout Success | Desktop | ![screenshot](documentation/images/testing/lighthouse/checkout_success.png)        | No major warnings   |
| Checkout Success | Mobile  | ![screenshot](documentation/images/testing/lighthouse/checkout_success_mobile.png) | Some minor warnings |
| Profile          | Desktop | ![screenshot](documentation/images/testing/lighthouse/profile.png)                 | No major warnings   |
| Profile          | Mobile  | ![screenshot](documentation/images/testing/lighthouse/profile_mobile.png)          | Some minor warnings |
| Orders           | Desktop | ![screenshot](documentation/images/testing/lighthouse/orders.png)                  | No major warnings   |
| Orders           | Mobile  | ![screenshot](documentation/images/testing/lighthouse/orders_mobile.png)           | Some minor warnings |

### Conclusion:

The Lighthouse audit has been instrumental in pinpointing areas where the site performs well and where improvements can be made. The areas identified for improvement, such as image optimization and resource minimization, are planned for future iterations of the site. The current focus has been to meet functionality requirements within a strict deadline, with performance optimizations slated for subsequent updates.

## Manual Testing

| Page                      | User Action                                                                           | Expected Result                                                                                              | Pass/Fail | Comments                                                            |
|---------------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------|
| **Home Page and Navbar**  |                                                                                       |                                                                                                              |           |                                                                     |
|                           | Click on Logo                                                                         | Redirection to Home page                                                                                     | Pass      |                                                                     |
|                           | Click on Home button in navbar                                                        | Redirection to Home page                                                                                     | Pass      |                                                                     |
|                           | Click on Products button in navbar                                                    | Redirection to Products page                                                                                 | Pass      |                                                                     |
|                           | Click on Contact button in navbar                                                     | Redirection to Contact us page                                                                               | Pass      |                                                                     |
|                           | Click on Search icon in navbar                                                        | Shows a searchbar                                                                                            | Pass      |                                                                     |
|                           | Click on Wishlist icon in navbar                                                      | Redirection to Wishlist page (if logged in) and vise-versa                                                   | Pass      |                                                                     |
|                           | Click on Bag icon in navbar                                                           | Redirection to Bag page                                                                                      | Pass      |                                                                     |
|                           | Click on Profile icon in navbar                                                       | Redirection to Profile page                                                                                  | Pass      |                                                                     |
|                           | Click on each Product in Top Products                                                 | Redirection to Product detail page                                                                           | Pass      |                                                                     |
|                           | Click on Products heart icon                                                          | Adds Products to Wishlist (if logged in)                                                                     | Pass      |                                                                     |
|                           | Fill out and click sign up (newsletter form)                                          | Adds email to db, and send mail confirmation                                                                 | Pass      |                                                                     |
|                           | Try to subscribe to newsletter with already subscribed email address                  | Error message appears telling user to check the form or make sure they're not already subscribed             | Pass      |                                                                     |
| **Footer**                |                                                                                       |                                                                                                              |           |                                                                     |
|                           | Click Home link in footer                                                             | Redirects user to Home page                                                                                  | Pass      |                                                                     |
|                           | Click Contact link in footer                                                          | Redirects user to contact page                                                                               | Pass      |                                                                     |
|                           | Click social media (Facebook) in footer                                               | Opens social media site clicked in a new tab                                                                 | Pass      |                                                                     |
|                           | Click on Products in footer                                                           | Redirection to Products page                                                                                 | Pass      |                                                                     |
|                           | Click on About in footer                                                              | Redirection to Home page and scrolling to About section                                                      | Pass      |                                                                     |
| **Products Page**         |                                                                                       |                                                                                                              |           |                                                                     |
|                           | Click on each Categories                                                              | Filters products and shows related Products                                                                  | Pass      |                                                                     |
|                           | Click on Products heart icon                                                          | Adds Products to Wishlist (if logged in) and vise-versa                                                      | Pass      |                                                                     |
|                           | Click on each Product                                                                 | Redirection to Product detail page                                                                           | Pass      |                                                                     |
|                           | Click on pages link in pagination                                                     | Shows related to that link page                                                                              | Pass      |                                                                     |
| **Product Detail Page**   |                                                                                       |                                                                                                              |           |                                                                     |
|                           | Click on Products heart icon                                                          | Adds Products to Wishlist (if logged in)                                                                     | Pass      |                                                                     |
|                           | Click + button on quantity selector form                                              | Quantity number increases to maximum to Product qty in stock                                                 | Pass      |                                                                     |
|                           | Click - button on quantity selector form                                              | Quantity number decreases to minimum one                                                                     | Pass      |                                                                     |
|                           | Click Add To Cart button                                                              | Product is added to cart and quantity is set to the user's choice                                            | Pass      |                                                                     |
|                           | Click Add To Cart button when user already has the product in their basket            | Quantity selected is added to the existing quantity in the user's cart for the product                       | Pass      |                                                                     |
|                           | Click on edit product button                                                          | Redirection to Edit Product page for that product (as admin)                                                 | Pass      | only appears if logged in user is an admin                          |
|                           | Click on delete product button                                                        | Redirection to Delete Product page (as admin)                                                                | Pass      | only appears if logged in user is an admin                          |
| **Searchbar**             |                                                                                       |                                                                                                              |           |                                                                     |
|                           | Enter word into search bar that appears in at least one product's name or description | Redirection to Products page                                                                                 | Pass      | Products filtered to only show products containing search term      |
|                           | Enter word into search bar that doesn't appear in any product's name or description   | Redirection to Products page                                                                                 | Pass      | Products page is empty and shows user that 0 products were returned |
|                           | Enter nothing into search bar                                                         | Redirection to Products page                                                                                 | Pass      |                                                                     |
| **Contact Page**          |                                                                                       |                                                                                                              |           |                                                                     |
|                           | Enter name                                                                            | Form will only submit if all fields are filled                                                               | Pass      |                                                                     |
|                           | Enter valid email address                                                             | Field will only accept email address format                                                                  | Pass      |                                                                     |
|                           | Enter message                                                                         | Form will only submit if all fields are filled                                                               | Pass      |                                                                     |
|                           | Click Send with missing fields                                                        | Message lets user know all fields are required                                                               | Pass      |                                                                     |
|                           | Click Send with all valid fields                                                      | User is sent email confirming their message has been received and information has been saved in the database | Pass      |                                                                     |
| **Sign Up Page**          |                                                                                       |                                                                                                              |           |                                                                     |
|                           | Enter valid email address                                                             | Field will only accept email address format                                                                  | Pass      |                                                                     |
|                           | Enter valid password (twice)                                                          | Field will only accept password format                                                                       | Pass      |                                                                     |
|                           | Click Sign Up button on sign up page                                                  | Sends confirmation email and lets user know to check their email                                             | Pass      |                                                                     |
|                           | Click link in confirmation email                                                      | Redirects user to sign in page                                                                               | Pass      |                                                                     |
| **Sign In Page**          |                                                                                       |                                                                                                              |           |                                                                     |
|                           | Enter valid email address                                                             | Field will only accept email address format                                                                  | Pass      |                                                                     |
|                           | Enter valid password                                                                  | Field will only accept password format                                                                       | Pass      |                                                                     |
|                           | Click Login button on login page                                                      | Redirects user to homepage                                                                                   | Pass      |                                                                     |
| **Log Out Page**          |                                                                                       |                                                                                                              |           |                                                                     |
|                           | Click Logout button                                                                   | Redirects user to logout and asks for confirmation that the user wants to log out page                       | Pass      |                                                                     |
|                           | Click Logout button                                                                   | Redirects user to home page                                                                                  | Pass      |                                                                     |
| **User Profile Page**     |                                                                                       |                                                                                                              |           |                                                                     |
|                           | Click Orders to see previous orders in Order History                                  | Redirects user to order history section                                                                      | Pass      |                                                                     |
|                           | Click Add Product to website (as admin)                                               | Redirects to Add Product page                                                                                | Pass      |                                                                     |
|                           | Click Change Password                                                                 | Redirects to Change Password page                                                                            | Pass      |                                                                     |
|                           | Click Logout button                                                                   | Redirects to Logout confirmation page                                                                        | Pass      |                                                                     |
| **Bag**                   |                                                                                       |                                                                                                              |           |                                                                     |
|                           | Click Continue shopping link (if bag is empty)                                        | Redirects to Products                                                                                        | Pass      |                                                                     |
|                           | Click Checkout button                                                                 | Redirects to Checkout page                                                                                   | Pass      |                                                                     |
|                           | Click + button on quantity selector form                                              | Quantity number increases to maximum to Product qty in stock                                                 | Pass      |                                                                     |
|                           | Click - button on quantity selector form                                              | Quantity number decreases to minimum one                                                                     | Pass      |                                                                     |
|                           | Click update button                                                                   | Updated quantity of product in cart to number in quantity select form                                        | Pass      |                                                                     |
|                           | Click remove button                                                                   | Removes product from cart                                                                                    | Pass      |                                                                     |
| **Checkout**              |                                                                                       |                                                                                                              |           |                                                                     |
|                           | Click Complete Order button without all required fields filled out                    | Brings back to the form                                                                                      | Pass      |                                                                     |
|                           | Click Complete Order button without card details filled out                           | Message letting user know that their card number is incomplete                                               | Pass      |                                                                     |
|                           | Click Complete Order button with all details filled out                               | Loading spinner appears and order is processed                                                               | Pass      |                                                                     |
|                           | Order completed                                                                       | Order confirmation email is sent to the user and redirection to checkout success page                        | Pass      |                                                                     |
| **Add Product Page**      |                                                                                       |                                                                                                              |           |                                                                     |
|                           | Click Cancel button                                                                   | Redirects admin to products page                                                                             | Pass      |                                                                     |
|                           | Click Add Product button with form filled correctly                                   | Creates a new product on the site using the information provided                                             | Pass      |                                                                     |
|                           | Click Add Product button with form filled incorrectly                                 | Message appears letting the admin know to fill in the required form fields                                   | Pass      |                                                                     |
| **Edit Product Page**     |                                                                                       |                                                                                                              |           |                                                                     |
|                           | Click Cancel button                                                                   | Redirects admin to all products page                                                                         | Pass      |                                                                     |
|                           | Click Update Product button with form filled correctly                                | Updates product with information provided                                                                    | Pass      |                                                                     |
|                           | Click Update Product button with form filled incorrectly                              | Message appears letting the admin know to fill in the required form fields                                   | Pass      |                                                                     |

## User Story Testing

| User Story                                                                                                                                                                     | Screenshot                                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| *"As an Administrator, I can organize products into categories, so that customers can easily browse products based on their interests."*                                       | ![User Story](documentation/images/user_stories/categories.png)          |
| *"As an Administrator, I can add new products to the inventory, so that customers have access to the latest musical instruments."*                                             | ![User Story](documentation/images/user_stories/add_product.png)         |
| *"As an Administrator, I can update existing product details, so that the product information is accurate and up-to-date."*                                                    | ![User Story](documentation/images/user_stories/edit_product.png)        |
| *"As an Administrator, I can remove products from the inventory, so that products that are no longer available are not displayed to customers."*                               | ![User Story](documentation/images/user_stories/delete_product.png)      |
| *"As a Customer, I can browse through the list of available products, so that I can find the instrument that I am interested in purchasing."*                                  | ![User Story](documentation/images/user_stories/products.png)            |
| *"As a Customer, I can view detailed information about a product, so that I can make an informed decision about purchasing it."*                                               | ![User Story](documentation/images/user_stories/product_detail.png)      |
| *"As a Customer, I can add and remove products from my shopping cart, so that I can manage the products I am interested in buying."*                                           | ![User Story](documentation/images/user_stories/product_bag.png)         |
| *"As a Customer, I can go through a checkout process, so that I can purchase my selected musical instruments."*                                                                | ![User Story](documentation/images/user_stories/checkout.png)            |
| *"As a Customer, I can pay for my purchases through a secure payment system, so that I can complete transactions with confidence."*                                            | ![User Story](documentation/images/user_stories/stripe_payment.png)      |
| *"As a Customer, I can track the status of my orders, so that I know when to expect the delivery of my products."*                                                             | ![User Story](documentation/images/user_stories/orders.png)              |
| *"As a Visitor, I can register for a new user account, so that I can start purchasing products and track my orders."*                                                          | ![User Story](documentation/images/user_stories/register.png)            |
| *"As a User, I can log in and out of my account, so that I can access my personal account information securely."*                                                              | ![User Story](documentation/images/user_stories/login.png)               |
| *"As a User, I can manage my profile information, so that my shipping and billing information is up-to-date."*                                                                 | ![User Story](documentation/images/user_stories/pass_recovery.png)       |
| *"As a User, I can recover my forgotten password, so that I can regain access to my account."*                                                                                 | ![User Story](documentation/images/user_stories/profile.png)             |
| *"As a Customer, I can contact the store through a form, so that I can report issues or ask for information."*                                                                 | ![User Story](documentation/images/user_stories/contact.png)             |
| *"As a User, I want to be able to create my own wishlist to save products that I plan to purchase in the future."*                                                             | ![User Story](documentation/images/user_stories/wishlist_create.png)     |
| *"As a User, I want to add products to the wishlist with a single click so that I can easily manage my preferences."*                                                          | ![User Story](documentation/images/user_stories/wishlist_add.png)        |
| *"As a User, I want to view my wishlist so that I can see all the items I've marked in one place."*                                                                            | ![User Story](documentation/images/user_stories/wishlist_management.png) |
| *"As a User, I want to be able to remove products from my wishlist and adjust their quantities to manage my wishlist according to my changing needs or preferences."*          | ![User Story](documentation/images/user_stories/wishlist_remove.png)     |
| *"As a Designer, I want to create the layout for the homepage so that it is visually appealing and functional for users."*                                                     | ![User Story](documentation/images/user_stories/home_design.png)         |
| *"As a Marketing Specialist, I want top products to be highlighted on the homepage to draw attention to our best offerings."*                                                  | ![User Story](documentation/images/user_stories/top_products.png)        |
| *"As a User, I want to use a search function to find products quickly, so that I can more efficiently discover items that I am interested in purchasing."*                     | ![User Story](documentation/images/user_stories/searchbar.png)           |
| *"As a User, I want to use filters, such as category, brand, price range, and ratings, so that I can narrow down the search results to find exactly what I am looking for."*   | ![User Story](documentation/images/user_stories/filtering.png)           |

## Bugs

### Fixed Bugs

#### Stripe Payments and Webhook Issue

**Description**

I encountered a specific bug related to Stripe payments and webhook handling. The issue arose with orders involving products on sale and when the delivery charge was 10€ (for orders below 100€).

![Bugs screenshot](documentation/images/bugs/webhooks_error.png)

**Resolution**

1. Order Model - Update Total Method:<br><br>
I updated the update_total method in the Order model. This method now correctly aggregates the line item prices, including any additional calculations for delivery costs based on the order total.

Updated update_total method:
```
def update_total(self):
    """
    Update the order total by aggregating the prices of the line items.
    This should also include the delivery cost if applicable.
    """
    self.total = sum(lineitem.lineitem_total for lineitem in self.items.all())
    if self.total < settings.FREE_DELIVERY_THRESHOLD:
        self.delivery = settings.STANDARD_DELIVERY_PRICE
    else:
        self.delivery = 0

    self.grand_total = self.total + self.delivery
    self.save()
   ```

2. OrderLineItem Model - Save Method:<br><br>

    I also revised the save method in the OrderLineItem model. The method now handles the discounted price calculation if the product is on sale and updates the line item total accordingly.

Updated save method:
```
def save(self, *args, **kwargs):
    """
    Override the original save method to set the lineitem total
    and update the order total.
    """
    if self.product.discount_percentage:
        discount = (self.product.price * self.product.discount_percentage / 100)
        discounted_price = self.product.price - discount
        self.price = discounted_price
        self.lineitem_total = discounted_price * self.quantity
    else:
        self.lineitem_total = self.product.price * self.quantity
    super().save(*args, **kwargs)
   ```

![Solved Bug screenshot](documentation/images/bugs/webhooks_success.png)

**Conclusion:**

The modifications were successful in resolving the issue. The Stripe dashboard now shows all payment requests as successful, indicating that the payment and webhook system is now functioning correctly for all scenarios, including discounted products and applicable delivery charges.

![Stripe Dashboard](documentation/images/bugs/stripe_dashboard.png)

### Unfixed Bugs

#### Payment Processing with Stripe

**Description**

A notable issue remains unresolved in the M-TUNE project regarding Stripe's payment processing integration. This issue is detailed under the "Payment Processing with Stripe" section in the README.md.

**Details of the Issue**

The current Stripe integration works, but it has been identified that the client-side confirmation of payments through JavaScript, as taught in the Boutique Ado project, may not be adequate for real-world application, particularly in handling invalid payment data robustly and reflecting these validations accurately in the user interface.

**Current Limitation**

Presently, when invalid payment data is entered, Stripe may handle the data correctly on the backend, but the user interface might not accurately reflect the backend validation. This can lead to situations where the payment appears successful in Stripe's system, but the user receives an error message.

**Planned Improvements**

- **Transition to Backend Validation**: I plan to shift from client-side to server-side validation for payments to align with Stripe's best practices. This will ensure the payment process is only completed after thorough backend validation.

- **In-Depth Stripe Integration**: The project aims to delve deeper into Stripe's documentation to leverage its full capabilities, implementing a more robust payment system.

- **Rigorous Testing**: Continuous testing will be carried out for various checkout scenarios to ensure a seamless user experience.

For more information on this issue and the detailed plans for addressing it, please refer to the [🔥 Important: Payment Processing with Stripe section in the readme.md.](https://github.com/GenaPlem/django_music_store?tab=readme-ov-file#-important-payment-processing-with-stripe)

---
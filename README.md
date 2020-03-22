# testPlanCreation
- Tool that indicates which tests should not be included in the Regression Test Plans and the ones that should be
Note: Only work with CIn/Motorola VPN.

The application was developed using:
- Python 3.3
- Django 1.8

Steps to use:
# Step 1:
  - Open a browser on this adress: 127.0.0.1:8000
  - Log in with a CoreId

# Step 2:
  - Create a Test Plan manually at Dalek and input the key on the indicated field.
  - Input the Regression Level (use a comma to separate).
  - Copy a link of the Google spreadsheet that contain the Product Checklist.
  Note¹: Has to be a "Google Spredsheet". If the file has .xls extension, it will not work.
  Note²: It's necessary to share the spreadsheet with: "testplancreation@testplancreate.iam.gserviceaccount.com"

# Step 3:
  - From the list, choose a category (only one).

# Step 4:
  - From the list, choose a subcategory (only one).

# Step 5:
- From the list choose a filter (only one)
Note³: If you choose on step 4 "DMT" you can choose more than one filter.
       If you choose on step 4 "Experiences" step 5 will not be necessary.

# Step 6:
  - Results will be shown on the screen.
  


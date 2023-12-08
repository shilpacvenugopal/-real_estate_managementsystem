# Real Estate Management System

## Installation

Follow these steps to set up the Real Estate Management System project on your local machine.

### Prerequisites

- [Python](https://www.python.org/) (version 3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/shilpacvenugopal/real_estate_managementsystem.git
   cd real-estate-management
   ```

2. **Create a Virtual Environment:**

   ```bash
   virtualenv venv
   ```

3. **Activate the Virtual Environment:**

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run Migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create Superuser (Admin User):**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create an admin user.

7. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   The project will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

8. **Access the Admin Interface:**

   Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with the admin credentials created in step 6.
   username: user1@gmail.com
   password - 1234

## Technology Stack

- **Backend:** Python – Django
- **Frontend:** Django Templates
- **Database:** PostgreSQL


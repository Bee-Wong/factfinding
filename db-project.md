# <p style="text-align: center;"><span style="font-family: Times New Roman; font-size: 3em;"> Database </span>


<p align="center"> <img src="https://miro.medium.com/v2/resize:fit:750/0*rwqI3XKmDZgsVuxr.jpg" alt="drawing" width="900" height="500"/> </p>

###### Task: Activity - Introduction to Database

### <span style="color:#FF5733">Exercise 1</span>

## <span style="color:#FF5733">Information Needed from Project Stakeholders </span>
- Inventory details: What specific information about books, including titles, authors, ISBN, quantity, and pricing, needs to be tracked?
- Sales reports: What data should be included in sales reports, and how frequently should they be generated?
- Author and performer appearance schedules: What details about appearances, such as dates, times, and participants, should be recorded?
- User access requirements: Who are the users (bookstore owners and employees), and what level of access and permissions do they need?


<p align="center"> <img src="https://chronicle.brightspotcdn.com/dims4/default/e1f7390/2147483647/strip/true/crop/1145x763+0+76/resize/1680x1120!/format/webp/quality/90/?url=http%3A%2F%2Fchronicle-brightspot.s3.us-east-1.amazonaws.com%2Ffa%2Fd3%2Fcd37ed9725291dd4767c1c12bdc4%2Fr-badboard-istock-0000515194056.jpg" width="900" height="500"/> </p>

## <span style="color:#FF5733">Interactions with Customers and Stakeholders </span>
To ensure a successful database design process, the following interactions will be essential:
- Initial meetings: Conduct meetings with project stakeholders to gather and clarify requirements.
- Requirement elicitation: Engage in discussions and interviews to capture detailed requirements for each database component (inventory, sales, schedules, and user access).
- Prototyping: Create prototype designs and solicit feedback to validate the design choices.
- Progress updates: Provide regular updates to stakeholders on the project's status, addressing questions and concerns.
- Testing and validation: Collaborate with stakeholders for user acceptance testing to ensure the database meets their needs.

### <span style="color:#FF5733">Exercise 2</span>

# <span style="color:#FF5733">Provided Resources and Additional Questions </span>

## <span style="color:#FF5733">Provided Resources </span>
The stakeholders have provided the following resources:
- **New Inventory Form**: A paper form used to collect information about new titles received by the store. This form is used by one of the managers to update the inventory spreadsheet.

- **Inventory Spreadsheet**: A shared spreadsheet that contains a list of all the inventory owned by the store.

- **Customer Receipt**: An example of a sales receipt given to customers after a purchase.

- **Monthly Sales Report**: A monthly sales report produced manually by one of the managers and provided to store owners and the management team.

## <span style="color:#FF5733">Additional Questions for Store Managers </span>
In order to better understand the data sources and gather necessary information for the database design, the following questions should be asked to store managers:
1. **New Inventory Form**:
   - What specific data fields are captured on the new inventory form?
   - How frequently is this form used to update the inventory spreadsheet?
   
2. **Inventory Spreadsheet**:
   - What columns and information are included in the inventory spreadsheet?
   - Is there a unique identifier for each book in the inventory?
   
3. **Customer Receipt**:
   - What details are present on the customer receipt, and which of these should be recorded in the database?
   
4. **Monthly Sales Report**:
   - What data is included in the monthly sales report, and can it be used as a template for the database's sales report feature?

###  <span style="color:#FF5733">Exercise 3</span>

# <span style="color:#FF5733">Data Requirements for Inventory Tracking </span>

## <span style="color:#FF5733">New Inventory Form</span>
- Primary Pieces of Information:
  - Book Title
  - Author
  - ISBN
  - Quantity Received
  - Pricing

- Annotations:
  - Book Title: Word
  - Author: Word
  - ISBN: Word
  - Quantity Received: Standard Numeric Format
  - Pricing: Decimal Format

##  <span style="color:#FF5733">Inventory Spreadsheet</span>
- Primary Pieces of Information:
  - Book Title
  - Author
  - ISBN
  - Quantity Owned
  - Pricing

- Annotations:
  - Book Title: Word
  - Author: Word
  - ISBN: Word
  - Quantity Owned: Standard Numeric Format
  - Pricing: Decimal Format

## <span style="color:#FF5733">Sales Receipt </span>
- Primary Pieces of Information:
  - Date of Sale
  - Book Title(s)
  - Quantity Sold
  - Total Price

- Annotations:
  - Date of Sale: Standard Numeric Format (assuming date)
  - Book Title(s): Word
  - Quantity Sold: Standard Numeric Format
  - Total Price: Decimal Format

##  <span style="color:#FF5733">Monthly Sales Report</span>
- Primary Pieces of Information:
  - Date
  - Total Sales Amount
  - Book Titles Sold
  - Quantity Sold for Each Book

- Annotations:
  - Date: Standard Numeric Format (assuming date)
  - Total Sales Amount: Decimal Format
  - Book Titles Sold: Word
  - Quantity Sold for Each Book: Standard Numeric Format

## <span style="color:#FF5733">Event Schedule </span>
- Primary Pieces of Information:
  - Event Date
  - Author/Performer Name
  - Event Type
  - Event Location

- Annotations:
  - Event Date: Standard Numeric Format (assuming date)
  - Author/Performer Name: Word
  - Event Type: Word
  - Event Location: Word



<p style="text-align: center;"><span style="font-family: Times New Roman; color:#FF5733"> Room 1 - Hawa . Hani . Hamza . Khalid . Beewong </span>

<p align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/SNice.svg/640px-SNice.svg.png" width="200" height="200"/> </p>



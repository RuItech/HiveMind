# Hivemind Architecture

Hivemind is an API that provides basic club management functionalities to a project.

This functionality is provided via its :

## Models

*UserProfile Model* : This model represents a Users Profile. It'll hold the following fields/properties :

- **User** :: Foreign Key - This will be the link between a User Profile and a Django User.

- **First Name** :: String - This will represent the Users First Name.

- **Last Name** :: String - This will represent the Users Last Name.

- **Next Payment Deadline** :: *TBD* - This field/property will hold the next membership payment deadline.

- **School ID** :: *Unique* String - This is the Students/Members School Identification.

- **Email** :: String - This will represent the Users Email.

- **Phone Number** :: Phone Number - This will represent the Users Phone Number.

- **Active Member** :: Boolean - This will represent the Members Current Membership status.

*Payments Model* : This model represents the Membership Payments. It'll hold the following fields/properties :

- **UserProfile** :: Foreign Key - This will be the link between a Payment and The User who made it.

- **Payment Reference** :: *Unique* String - This will be the Payments Reference or Identification Number.

- **Payment Duration** :: *TBD* - This will be the Duration at which a member has paid for their membership.

- **Payment Made On** :: DateTime - This will be auto generated on creation of a Payment.

- **Additional Comment** :: *Optional* String - This field will contain any additional comments referring to the payment.

*Event Model* : This model represents the Events. It'll hold the following fields/properties :

- **Event Name** :: String - This will be the events name.

- **Event Description** :: String / Text Field - This will represent the Events Description.

- **Event Start Time** :: DateTime - This will represent the Events Start Name.

- **Event End Time** :: DateTime - Thiw will represent the Events End Time.

*News Model* : This model represents the News. It'll hold the following fields/properties : 

- **News Headline** :: String - This represents the News Headline.

- **News Details** :: String / TextField - This represents the News Details.

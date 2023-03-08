# Cheat-sheet ##


### What is an API?
APIs (application programming interfaces)

An API is the tool that makes a website's data digestible for a computer. Through it, a computer can view and edit data, just like a person can by loading pages and submitting forms.

API is provided by the server.

When one site pulls in data from the other, the site providing the data is acting as the server, and the site fetching the data is the client.

### JSON Format
List with values that have names

### XML Format

### HTTP Request:
Communication in HTTP centers around a concept called the Request-Response Cycle. The client sends the server a request to do something. The server, in turn, sends the client a response saying whether or not the server could do what the client asked.

The client has to include the following things:
  * URL

    A unique address for a thing. official name: resource

    Url's are a easy way for the cloent to tell the server which thin it wants to interact with.
  * Methods

    GET - Asks the server to retrieve a resource

    POST - Asks the server to create a new resource

    PUT - Asks the server to edit/update an existing resource
    
    DELETE - Asks the server to delete a resource

  * Headers

    They provide meta-information about a request. They are a simple list of items like the time the client sent the request and the size of the request body.
  * Body

    The request body contains the data the client wants to send the server. This is the only part of the request the client has complete control over .

![](docs/pictures2/http.PNG)

### HTTP Status Codes

### Endpunkte

### Polling
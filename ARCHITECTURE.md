# Overall Architecture

This app was designed with the purpose to be the generic tax calculator application that can be used by everyone on the internet.

# Frontend Architecture

- Entry Point: `app/page.tsx`
- Components: `components/*`
- Utilities: `lib/*`.\
  To separate generic utility functions

# Backend Architecture

- Entry Point: `api/index.py`
- database models and it's related things: `api/model`.\
  Every model have at most 3 representations or classes.

  - 1 "dumb" class.\
    This class job is to mimick the database fields.
  - 1 "smart" class.\
    This class's job is to provde behaviour that for the "dumb" class.
  - 1 "Manager" class.\
    This class's job is to provides behaviour that takes care the database related things.

- domain driven services and it's related things: `api/*`. Example: `api/entries`\
  There are 2 types of class:
  - Service \
    This class's job is to take care all the business logic for the domain. This way, we won't clutter the endpoint with business logic. The other benefit is that we can also encapsulate the business layer from the other layer such as application layer, etc.
  - DTO \
    This class's job is to provide a contract between the client and the api endpoint. This way, we can make the contract between the client and the endpoint more safe, clear, and maintainable

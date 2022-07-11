## Python Interface to SpaceX API at https://github.com/r-spacex/SpaceX-API

### Description

Essentially takes the data from the SpaceX API and bundles it into an easy to use python interface for accessing the data.

## Getting Started


### Dependencies

Python 3.8+

### Installing

Clone the repo via your preferred method
Create a virtual envirnoment, for eg
``` python3.8 -m virutalenv env ```

Activate virtual envirnoment
``` source/env/bin/activate ```

Install dependencies
``` pip install -r requirements.txt ```

The class is now ready to use!

### Using the code

Simply instatiate the class and call desired methods.

For eg.

``` 
spacexapi = SpaceXAPIInterface()
company_info = spacexapi.get_company_info()
```
    
This returns the current company info from the SpaceX API which can be accessed pythonically using a variation of lists and dicts. (The easiest way to figure out which syntax to use is to print the result of the method call to the console and observe it's structure)


## Authors

_Michael Telford_ <br></br>
https://github.com/MTelford/


## License

This project is licensed under the MIT License - see the LICENSE.md file for details


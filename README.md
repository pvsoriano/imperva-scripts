# Imperva Scripts

This is a collection of various Imperva cloud WAF scripts to help manage your website profiles. Below are the two scripts that I've written so far:

* **incap-allow-ips.py**: Script that takes a list of IP addresses in a text file and enters them into the exception (allowed) list of the blocked IP's section of a WAF profile security section.

* **incapsula_block_ips.py**: Script that takes in a list of IP addresses in a text file and enters them into the block IP section of a WAF profile security section.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You'll need to have Python 3 installed and the following modules:

* json
* urllib
* pprint
* argparse
* sys

### Installing

You can clone or fork the repo, or copy the code into a file on your system.

You'll need to provide the following information within the script in order to run it:

* **api_id**: ID number of the API key that Imperva provides to you when you create a new API key in the "Settings" section of Account Users
* **api_key**: Actual API key that Imperva provides when you create it.
* **site_id**: This is the WAF profile within Imperva that you'll be updating

## Deployment

The script will take a list of IP addresses as input. Each IP address must be on a separate line in the text file. You can run the script as follows:

```
python3 incap-allow-ips.py <NAME OF IP LIST FILE>.txt
```

## Built With

* [Python](https://www.python.org) - Language used to build the script

## Features
List of features:
* Import a lot of IP's into an exception or block list on a WAF profile easily, instead of doing it via the web GUI.

To-do list:
* Prompt user to input the site_id instead of manually entering within the script itself.
* Find a better way to securely pull api_id or api_key into the script (could just prompt the user as well).
* Combine the scripts into one and have a menu option to pick what you want to do (add IP's to exception or block list)
* Add logic to check if IP's already exist in the profile, and if so, append instead of overwriting all IP addresses

## Contributing

Feel free to contribute if you'd like.

## Versioning

There's no versioning yet.

## Authors

* **Paul Soriano** - *Initial work* - [pvsoriano](https://github.com/pvsoriano)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Kudos to Imperva engineers that provided me the initial Python script to build off of.

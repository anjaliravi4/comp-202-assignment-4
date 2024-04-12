
class Company:
    '''
    Represents a company
    Attributes:
        name (str): name of the company
        location (str): location of company
    '''
    
    
    def __init__(self, name, location):
        '''
        (str, str) -> Company
        Creates a Company object and initializes its name and location
        
        Example 1:
        >>> c1 = Company('Pear', 'Chicago')
        >>> print(c1.name, c1.location)
        Pear, Chicago
        
        Example 2:
        >>> c2 = Company('A4 Entertainment', 'Boston')
        >>> print(c2.name)
        A4 Entertainment
        
        Example 3:
        >>> c3 = Company('Align', 'Austin')
        >>> print(c3.location)
        Austin
        '''
        
        #initializing name and location
        self.name = name
        self.location = location
     
     
    def update_location(self, new_location):
        '''
        (str) -> None
        Updates the location of an existing Company object
        
        Example 1:
        >>> c1.update_location('Paris')
        >>> print(c1.location)
        Paris
        
        Example 2:
        >>> c2.update_location('Dallas')
        >>> print(c2.location)
        Dallas
        
        Example 3:
        >>> c4.update_location('Los Angeles')
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'c4' is not defined
        '''
        #updating location
        self.location = new_location
        
        
class JobOffer:
    '''
    Represents details of a job offer
    Attributes:
        title (str): title of job offer
        description (str): position description
        company (company): company presenting the job offer
        contract (str): type of contract
        salary (int): salary of job offer
    '''
    def __init__(self, title, company, contract, salary, description):
        '''
        Creates JobOffer object and initializes its title, company, contract,
        salary, and description
        (str, Company, str, int, str) -> JobOffer
        
        Example 1:
        >>> offer1 = JobOffer('Software Engineer', c1, 'Permanent', 120000,
        'Full time SWE position')
        >>> print(offer1.salary)
        120000
        
        Example 2:
        >>> offer1 = JobOffer('Software Engineer', c1, 'Permanent', 120000,
        'Full time SWE position')
        >>> print(offer1.title)
        Software Engineer
        
        Example 3:
        >>> offer2 = JobOffer('Social Media Manager', c2, 'Permanent', 60000,
        'Social media manager position')
        >>> print(offer2.contract)
        Permanent
        '''
        #initializing attributes
        self.title = title
        self.company = company
        self.contract = contract
        self.salary = salary
        self.description = description
        
        
    def update_description(self, new_description):
        '''
        (str) -> None
        Updates existing JobOffer with new description
        
        Example 1:
        >>> offer1.update_description('New description')
        >>> print(offer1.description)
        New description
        
        Example 2:
        >>> offer2.update_description('Options for remote or in-person')
        >>> print(offer2.description)
        Options for remote or in-person
        
        Example 3:
        >>> offer3.update_description
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'offer3' is not defined
        '''
        #updating description
        self.description = new_description
        
        
    def __str__(self):
        '''
        None -> str
        Changes str representation of JobOffer objects
        
        Example 1:
        >>> offer1 = JobOffer('Software Engineer', c1, 'Permanent', 120000,
        'Full time SWE position')
        >>> str(offer1)
        'Title: Software Engineer\nCompany: Pear\nLocation: Paris\nContract:
        Permanent\nDescription: Full time SWE position\nSalary: 120000' 
        
        Example 2:
        >>> offer1 = JobOffer('Software Engineer', c1, 'Permanent', 120000,
        'Full time SWE position')
        >>> print(offer1)
        Title: Software Engineer
        Company: Pear
        Location: Paris
        Contract: Permanent
        Description: Full time SWE position
        Salary: 120000
        
        Example 3:
        >>> offer2 = JobOffer('Social Media Manager', c1, 'Permanent', 60000,
        'Social media manager position')
        >>> str(offer2)
        'Title: Social Media Manager\nCompany: Pear\nLocation: Paris\nContract:
        Permanent\nDescription: Social media manager position\nSalary: 60000'
        '''
        #concatenating string with object attributes
        string = 'Title: ' + self.title + '\nCompany: ' + self.company.name +\
        '\nLocation: ' + self.company.location + '\nContract: '\
        + self.contract + '\nDescription: ' + self.description + '\nSalary: '\
        + str(self.salary)
        
        return string

    
def build_job_database(filePath):
    '''
    (str) -> (list, list)
    Reads given text file and takes info to create JobOffer and Company
    objects, and returns lists of all companies and job offers
    
    Example 1:
    >>> companyDB, offerDB = build_job_database('jobFile.txt')
    >>> companyDB[0].name
    Info4All
    
    Example 2:
    >>> companyDB, offerDB = build_job_database('jobFile.txt')
    >>> companyDB[1].location
    Calgary
    
    Example 3:
    >>> companyDB, offerDB = build_job_database('jobFile.txt')
    >>> offerDB[2].salary
    185000
    '''
    companyDB = []
    offerDB = []
    try:
        fobj = open(filePath, 'r')
        #iterating through each line in file and extracting necessary info
        for line in fobj:
            company_offer = line.split(',')
            title = company_offer[0]
            name = company_offer[1]
            location = company_offer[2]
            contract = company_offer[3]
            description = company_offer[4]
            salary = int(company_offer[5])
            #creating Company and JobOffer objects
            company = Company(name, location)
            offer = JobOffer(title, company, contract, salary, description)
            #adding Company and JobOffer objects to databases
            companyDB.append(company)
            offerDB.append(offer)
        fobj.close()
    #catching exceptions
    except FileNotFoundError:
        print('File does not exist')
    except:
        print('File corrupted or other issue')
    
    return companyDB, offerDB



        
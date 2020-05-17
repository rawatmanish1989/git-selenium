class LoginPage():
    
    def __init__(self, driver):
        self.driver = driver
    
    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    
    def getLoginLink(self):
        return self.driver.find_element_by_link_text(self._login_link)
    
    def getEmailField(self):
        return self.driver.find_element_by_id(self._email_field)
    
    def getPasswordField(self):
        return self.driver.find_element_by_id(self._password_field)
    
    def getLoginButton(self):
        return self.driver.find_element_by_name(self._login_button)
    
    #actions performed by the above returned objects
    def clickLoginLink(self):
        self.getLoginLink().click()
    
    def enterEmail(self, email):
        self.getEmailField().send_keys(email)
    
    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)
    
    def clickLoginButton(self):
        self.getLoginButton().click()
        
    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
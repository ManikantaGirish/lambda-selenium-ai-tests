import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# LambdaTest credentials from environment
LT_USERNAME = os.environ.get('LT_USERNAME')
LT_ACCESS_KEY = os.environ.get('LT_ACCESS_KEY')

class TestTummyTales:
    @pytest.fixture()
    def driver(self):
        # LambdaTest capabilities
        capabilities = {
            "build": "AI Test Automation",
            "name": "TummyTales Test",
            "platform": "Windows 10",
            "browserName": "Chrome",
            "version": "latest",
            "resolution": "1920x1080"
        }
        
        # Connect to LambdaTest
        grid_url = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@hub.lambdatest.com/wd/hub"
        driver = webdriver.Remote(
            command_executor=grid_url,
            desired_capabilities=capabilities
        )
        
        yield driver
        
        # Teardown
        driver.quit()
    
    def test_homepage_loads(self, driver):
        """Test that TummyTales homepage loads successfully"""
        driver.get("https://tummytales.info")
        driver.implicitly_wait(10)
        
        # Verify title
        assert "TummyTales" in driver.title or "tummytales" in driver.title.lower()
        
        # Mark test as passed
        driver.execute_script("lambda-status=passed")
    
    def test_navigation_exists(self, driver):
        """Test that navigation elements exist"""
        driver.get("https://tummytales.info")
        driver.implicitly_wait(10)
        
        # Check for common navigation elements
        nav_elements = driver.find_elements(By.TAG_NAME, "nav")
        assert len(nav_elements) > 0, "No navigation elements found"
        
        # Mark test as passed
        driver.execute_script("lambda-status=passed")
    
    def test_page_has_content(self, driver):
        """Test that page has content"""
        driver.get("https://tummytales.info")
        driver.implicitly_wait(10)
        
        # Check body has content
        body = driver.find_element(By.TAG_NAME, "body")
        assert len(body.text) > 0, "Page has no content"
        
        # Mark test as passed
        driver.execute_script("lambda-status=passed")

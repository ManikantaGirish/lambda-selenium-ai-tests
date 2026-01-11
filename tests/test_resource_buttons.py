import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestResourcePageButtons:
    """Test all buttons on TummyTales /resource page"""
    
    def setup_method(self):
        """Setup test with LambdaTest configuration"""
        username = os.environ.get('LT_USERNAME')
        access_key = os.environ.get('LT_ACCESS_KEY')
        
        lt_options = {
            "username": username,
            "accessKey": access_key,
            "build": "Resource Page Button Test",
            "name": "Test All Buttons on /resource",
            "platformName": "Windows 11",
            "browserName": "Chrome",
            "browserVersion": "latest"
        }
        
        options = webdriver.ChromeOptions()
        options.set_capability('LT:Options', lt_options)
        
        self.driver = webdriver.Remote(
            command_executor=f'https://{username}:{access_key}@hub.lambdatest.com/wd/hub',
            options=options
        )
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        
    def teardown_method(self):
        if self.driver:
            self.driver.quit()
    
    def test_all_resource_page_buttons(self):
        """Test all clickable buttons on /resource page"""
        self.driver.get('https://tummytales.info/resource')
        time.sleep(3)
        
        failed_buttons = []
        passed_buttons = []
        
        # Test filter buttons
        filter_buttons = [
            ('All', '//button[text()="All"]'),
            ('Articles', '//button[text()="Articles"]'),
            ('Videos', '//button[text()="Videos"]'),
            ('News', '//button[text()="News"]')
        ]
        
        for name, xpath in filter_buttons:
            try:
                button = self.driver.find_element(By.XPATH, xpath)
                button.click()
                time.sleep(1)
                passed_buttons.append(f'{name} filter button')
            except Exception as e:
                failed_buttons.append({
                    'button': f'{name} filter button',
                    'area': 'Filter section (top of page)',
                    'xpath': xpath,
                    'error': str(e)
                })
        
        # Test Search button
        try:
            search_btn = self.driver.find_element(By.XPATH, '//button[text()="Search"]')
            search_btn.click()
            time.sleep(1)
            passed_buttons.append('Search button')
        except Exception as e:
            failed_buttons.append({
                'button': 'Search button',
                'area': 'Search bar section',
                'xpath': '//button[text()="Search"]',
                'error': str(e)
            })
        
        # Test pagination buttons (first 3 pages)
        for i in range(1, 4):
            try:
                page_link = self.driver.find_element(By.XPATH, f'//a[text()="{i}"]')
                page_link.click()
                time.sleep(1)
                passed_buttons.append(f'Pagination button {i}')
            except Exception as e:
                failed_buttons.append({
                    'button': f'Pagination button {i}',
                    'area': 'Pagination section (bottom of page)',
                    'xpath': f'//a[text()="{i}"]',
                    'error': str(e)
                })
        
        # Test Previous/Next navigation
        nav_buttons = [
            ('Previous', '//a[contains(.,"Previous")]'),
            ('Next', '//a[contains(.,"Next")]')
        ]
        
        for name, xpath in nav_buttons:
            try:
                nav_btn = self.driver.find_element(By.XPATH, xpath)
                nav_btn.click()
                time.sleep(1)
                passed_buttons.append(f'{name} navigation button')
            except Exception as e:
                failed_buttons.append({
                    'button': f'{name} navigation button',
                    'area': 'Pagination navigation section',
                    'xpath': xpath,
                    'error': str(e)
                })
        
        # Test hamburger menu
        try:
            menu_btn = self.driver.find_element(By.XPATH, '//button[@aria-label="Open menu" or contains(@class,"menu")]')
            menu_btn.click()
            time.sleep(1)
            passed_buttons.append('Hamburger menu button')
        except Exception as e:
            failed_buttons.append({
                'button': 'Hamburger menu button',
                'area': 'Top navigation bar (mobile menu)',
                'xpath': '//button[@aria-label="Open menu"]',
                'error': str(e)
            })
        
        # Generate test report
        print("\n" + "="*60)
        print("BUTTON TEST REPORT - TummyTales /resource Page")
        print("="*60)
        print(f"\nTotal buttons tested: {len(passed_buttons) + len(failed_buttons)}")
        print(f"✓ Passed: {len(passed_buttons)}")
        print(f"✗ Failed: {len(failed_buttons)}")
        
        if passed_buttons:
            print("\n✓ PASSED BUTTONS:")
            for btn in passed_buttons:
                print(f"  ✓ {btn}")
        
        if failed_buttons:
            print("\n✗ FAILED BUTTONS:")
            for fail in failed_buttons:
                print(f"  ✗ Button: {fail['button']}")
                print(f"    Area: {fail['area']}")
                print(f"    XPath: {fail['xpath']}")
                print(f"    Error: {fail['error']}")
                print()
        
        # Assert that all buttons passed
        assert len(failed_buttons) == 0, f"{len(failed_buttons)} button(s) failed to click"

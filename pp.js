const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: true }); // Launches a browser with a visual interface
  const page = await browser.newPage(); // Opens a new page in the browser
  await page.goto('http://localhost:8080'); // Change the URL to your local server address

  // List of button IDs corresponding to each operation
  const buttonIds = [
    'clipboardButton',
    'cookieButton',
    'sessionStorageButton',
    'localStorageButton',
    'indexedDBButton',
    'serviceWorkerCacheButton',
  ];
  const button = buttonIds[2];

  try {
    console.log(`Clicking ${button}`); // Log which button is being clicked
    await page.click(`#${button}`); // Click each button by ID
    await new Promise((r) => setTimeout(r, 3000)); //
    console.log('All buttons clicked.'); // Confirm all buttons have been clicked
  } catch (error) {
    console.error('An error occurred:', error); // Log any errors that occur
  }

  await browser.close(); // Close the browser
  console.log('Browser closed.'); // Confirm the browser has closed
})();

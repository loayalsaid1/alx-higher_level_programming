const myImage = document.querySelector('img');

myImage.onclick = () => {
  const mySrc = myImage.getAttribute('src');

  if (mySrc === 'images/firefox-icon.png') {
    myImage.setAttribute('src', 'images/firefox2.jpg');
  } else {
    myImage.setAttribute('src', 'images/firefox-icon.png');
  }
};

const myButton = document.querySelector('button');
const myHeading = document.querySelector('h1');

/**
 * change user
 * Get the username
 * put it in the header
 *
 * and i also need to store it somewhere for next time the user comes
 */
function setUserName () {
  const myName = prompt('Please enter your name');
  if (!myName) {
    setUserName();
  } else {
    myHeading.textContent = `Mozilla is cool, ${myName}`;

    localStorage.setItem('name', myName);
  }
}

/**
 * if there is no name, then have one
 *
 * else:
 * 	add the previus name
 */
if (!localStorage.getItem('name')) {
  setUserName();
} else {
  const storedName = localStorage.getItem('name');
  myHeading.textContent = `Mozilla is cool, ${storedName}`;
}

myButton.onclick = () => {
  setUserName();
};

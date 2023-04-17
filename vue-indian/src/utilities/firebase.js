import * as firebase from "firebase/app";

import "firebase/auth";

const firebaseConfig = {

    apiKey: "AIzaSyBBPSsx_6i6boeV1zqAeRckBk0t4h73TK4",
    authDomain: "vue-f1d70.firebaseapp.com",
    projectId: "vue-f1d70",
    storageBucket: "vue-f1d70.appspot.com",
    messagingSenderId: "93658014770",
    appId: "1:93658014770:web:102693a293205f6eb1082b",
    measurementId: "G-LK521T0NNP"
};

firebase.initializeApp(firebaseConfig);

export default firebase;
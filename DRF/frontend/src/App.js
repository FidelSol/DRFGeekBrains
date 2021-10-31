import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
import AppFooter from './components/footer.js';
import AppMenu from './components/menu.js';
import axios from 'axios';

class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'authors': []
       }
   }

   componentDidMount() {
       axios.get('http://127.0.0.1:8000/api/v1/users')
           .then(response => {
               const authors = response.data
                   this.setState(
                   {
                       'authors': authors
                   }
               )
           }).catch(error => console.log(error))
    }


   render () {
       return (
           <div>
               <AppMenu />
               <AuthorList authors={this.state.authors} />
               <AppFooter />
           </div>


       )
   }
}


export default App;

import React from 'react';
import './App.css';
import UserList from './components/Users.js';
import ProjectList from './components/Projects.js';
import ProjectFilteredList from './components/Project.js'
import ToDoList from './components/ToDos.js';
import axios from 'axios';
import {BrowserRouter, Route, Link, Routes} from 'react-router-dom'

const NotFound404 = ({ location }) => {
  return (
    <div>
        <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  )
}



class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': [],
           'projects': [],
           'todos': []
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

            axios.get('http://127.0.0.1:8000/api/v1/presentprojects')
           .then(response => {
               const projects = response.data
                   this.setState(
                   {
                       'projects': projects
                   }
               )
           }).catch(error => console.log(error))

       axios.get('http://127.0.0.1:8000/api/v1/presenttodos')
           .then(response => {
               const todos = response.data
                   this.setState(
                   {
                       'todos': todos
                   }
               )
           }).catch(error => console.log(error))

    }


   render () {
       return (
            <div className="App">
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/todos'>ToDos</Link>
                            </li>
                        </ul>
                    </nav>
                    <Routes>
                            <Route path='/' element={() => <UserList items={this.state.users} />}  />
                            <Route path='/projects' element={() => <ProjectList items={this.state.projects} />} />
                            <Route path='/todos' element={() => <ToDoList items={this.state.todos} />} />
                            <Route path='/project/:id'>
                                <ProjectFilteredList items={this.state.projects} />
                            </Route>

                            <Route component={NotFound404} />
                    </Routes>
                </BrowserRouter>
            </div>


       )
   }
}


export default App;

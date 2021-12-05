import React from 'react';
import {Link} from 'react-router-dom'

const ProjectItem = ({item, deleteProject}) => {
   return (
       <tr>
           <td><Link to={`project/${item.id}`}>
               {item.id}</Link>
           </td>
           <td>
               {item.url}
           </td>
           <td>
               {item.name}
           </td>
           <td>
               {item.users}
           </td>
           <td><button onClick={()=>deleteProject(item.id)} type='button'>Delete</button></td>

       </tr>
   )
}

const ProjectList = ({projects, deleteProject}) => {
   return (
       <div>
       <table>
           <th>
               ID
           </th>
           <th>
               URL
           </th>
           <th>
               Name
           </th>
           <th>
               Users
           </th>
           {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject} />)}
       </table>
       <Link to='/projects/create'>Create</Link>
        </div>

   )
}

export default ProjectList





import React from 'react';
import {Link} from 'react-router-dom'

const ProjectItem = ({item}) => {
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
       </tr>
   )
}

const ProjectList = ({projects}) => {
   return (
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
           {projects.map((project) => <ProjectItem project={project} />)}
       </table>
   )
}

export default ProjectList





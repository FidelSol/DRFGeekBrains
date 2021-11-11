import React from 'react';
import { useParams } from 'react-router-dom'


const ProjectItem = ({item}) => {
    return (
        <tr>
           <td>
               {item.id}
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

const ProjectFilteredList = ({projects}) => {
    let { id } = useParams();
    let filtered_items = projects.filter((item) => item.id === id);

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
           {filtered_items.map((item) => <ProjectItem item={item} />)}
       </table>
    )
}

export default ProjectFilteredList





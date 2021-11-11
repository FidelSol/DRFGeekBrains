import React from 'react';

const ToDoItem = ({item}) => {
   return (
       <tr>
           <td>
               {item.id}
           </td>
           <td>
               {item.text}
           </td>
           <td>
               {item.project}
           </td>
           <td>
               {item.add_time}
           </td>
            <td>
               {item.mod_time}
           </td>
           <td>
               {item.creator}
           </td>
           <td>
               {item.status}
           </td>
       </tr>
   )
}

const ToDoList = ({todos}) => {
   return (
       <table>
           <th>
               ID
           </th>
           <th>
               Text
           </th>
           <th>
               Project
           </th>
           <th>
               Add Time
           </th>
           <th>
               Mod Time
           </th>
           <th>
               Creator
           </th>
           <th>
               Status
           </th>
           {todos.map((todo) => <ToDoItem todo={todo} />)}
       </table>
   )
}

export default ToDoList





import React from 'react';

const UserItem = ({item}) => {
   return (
       <tr>
           <td>
               {item.id}
           </td>
           <td>
               {item.first_name}
           </td>
           <td>
               {item.last_name}
           </td>
           <td>
               {item.email}
           </td>
       </tr>
   )
}

const UserList = ({users}) => {
   return (
       <table>
           <th>
               ID
           </th>
           <th>
               First name
           </th>
           <th>
               Last Name
           </th>
           <th>
               Email
           </th>
           {users.map((user) => <UserItem user={user} />)}
       </table>
   )
}

export default UserList





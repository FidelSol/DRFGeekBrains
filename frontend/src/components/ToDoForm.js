import React from 'react'


class ToDoForm extends React.Component {
    constructor(props) {
      super(props)
      this.state = {text: '', project: props.projects[0].id}
    }

    handleChange(event)
    {
        this.setState(
                {
                    [event.target.text]: event.target.value
                }
            );
    }

    handleSubmit(event) {
      this.props.createToDo(this.state.text, this.state.project)
      event.preventDefault()
    }


    render() {
      return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>
            <div className="form-group">
            <label htmlFor="text">text</label>
                <input type="text" className="form-control" name="text" value={this.state.text} onChange={(event)=>this.handleChange(event)} />
            </div>

        <div className="form-group">
            <label htmlFor="projects">projects</label>

            <select name="projects" className='form-control' onChange={(event)=>this.handleChange(event)}>
                {this.props.projects.map((item)=><option value={item.id}>{item.name}</option>)}
            </select>


          </div>
          <input type="submit" className="btn btn-primary" value="Save" />
        </form>
      );
    }
  }

  export default ToDoForm
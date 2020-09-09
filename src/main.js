//import 'fontsource-roboto';

var Split = require('split.js');
Split(['#one', '#two', '#three']);

var React = require('react');
var ReactDOM = require('react-dom');
var dragula = require('dragula');
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';

class ArticleList extends React.Component {
  render () {
    return (<div className="container" id="article-box">
    <Card>
      <CardContent>
        test
      </CardContent>
    </Card>
    <Card>
      <CardContent>
        test
      </CardContent>
    </Card>
    </div>
    );
  }
  componentDidMount () {
    let container = document.getElementById('article-box');
    dragula([container]);
  }
}
ReactDOM.render(<ArticleList />, document.getElementById('container'));

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box p={3}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired,
};

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

class TabDisplay extends React.Component {
  const value = React.useState(0), setValue = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  render () {
    return(<div className="container" id="three">
    <AppBar position="static">
      <Tabs value={value} onChange={handleChange} aria-label="simple tabs example">
        <Tab label="Item One" {...a11yProps(0)} />
        <Tab label="Item Two" {...a11yProps(1)} />
        <Tab label="Item Three" {...a11yProps(2)} />
      </Tabs>
    </AppBar>
    <TabPanel value={value} index={0}>
      Item One
    </TabPanel>
    <TabPanel value={value} index={1}>
      Item Two
    </TabPanel>
    <TabPanel value={value} index={2}>
      Item Three
    </TabPanel>
    </div>);
  }
}


ReactDOM.render(<TabDisplay />, document.getElementById('three'));

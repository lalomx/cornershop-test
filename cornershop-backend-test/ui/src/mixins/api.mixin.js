import axios from 'axios'
import moment from 'moment'

const URL = process.env.NODE_ENV === 'production'
  ? `${process.env.BASE_URL}api`
  : 'http://localhost:8000/lunch/api'

export default {
  methods: {
    getEmployees () {
      console.log(URL)
    },
    getMenus () {
      const week = moment().utc().isoWeek()
      return axios.get(URL + '/menu/week/' + week)
    },
    getOrders () {
      return axios.get(URL + '/order')
    },
    createMenu (menu) {
      return axios.post(URL + '/menu', menu)
    },
    editMenu (menu) {
      return axios.patch(URL + '/menu', menu)
    }
  }
}

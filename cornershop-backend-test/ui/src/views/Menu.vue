<template>
  <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-4 py-12">
    <div class="text-center pb-12">
      <h1
        class="
          font-bold
          text-3xl
          md:text-4xl
          lg:text-5xl
          font-heading
          text-gray-900
        "
      >
        Week menu
      </h1>
    </div>
    <div
      class="
        grid grid-cols-1
        sm:grid-cols-2
        md:grid-cols-2
        lg:grid-cols-5
        gap-6
      "
    >
      <div
        v-for="day in days"
        class="
          w-full
          bg-white
          rounded-lg
          sahdow-lg
          overflow-hidden
          flex flex-col
          justify-center
          items-center
          shadow-lg
        "
        :key="day.name"
      >
        <div class="text-center py-8 sm:py-6">
          <p class="text-xl text-gray-700 font-bold mb-2">{{ day.name }}</p>
          <ol v-if="day.menu" class="list-decimal">
            <li>{{day.menu.option_one}}</li>
            <li>{{day.menu.option_two}}</li>
            <li>{{day.menu.option_three}}</li>
            <li>{{day.menu.option_four}}</li>
          </ol>
          <p v-else>Not created</p>
        </div>
        <div class="text-left sm:py-6">
          <button @click="onClick(day)" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center">
            <span>{{ day.menu ? 'Edit' : 'Create' }}</span>
          </button>
        </div>
      </div>
    </div>
  <MenuCard :enabled="open" :menu="selectedMenu" @close="onClose" @submit="onSubmit"/>
  </section>
</template>

<script>
import moment from 'moment'
import _ from 'lodash'
import { v4 as uuidv4 } from 'uuid'

import api from '../mixins/api.mixin'
import MenuCard from '../components/MenuCard.vue'

export default {
  name: 'Menu',
  data () {
    return {
      menus: {},
      daysOfweek: [],
      open: false,
      selectedMenu: null
    }
  },
  mixins: [api],
  components: {
    MenuCard
  },
  async created () {
    const startOfWeek = moment().utc().startOf('isoWeek')
    const endOfWeek = moment().utc().endOf('isoWeek')
    let day = startOfWeek

    while (day <= endOfWeek) {
      this.daysOfweek.push(day.toDate())
      day = day.clone().add(1, 'd')
    }

    const { data } = await this.getMenus()
    this.menus = (_.groupBy(data.map(m => ({
      ...m,
      name: moment(m.date).format('dddd').toLowerCase()
    })),
    'name'))
  },
  computed: {
    days () {
      if (_.isEmpty(this.menus)) {
        return []
      }

      return this.daysOfweek.map(d => {
        const day = {
          name: moment(d).format('dddd').toLowerCase(),
          date: moment(d)
        }
        const menu = this.menus[day.name]
        if (menu) {
          day.menu = menu[0]
        }
        return day
      })
    }
  },
  methods: {
    onClick (day) {
      this.open = true
      this.selectedMenu = day.menu || { name: day.name }
    },
    onClose () {
      this.open = false
      this.selectedMenu = null
    },
    onSubmit (options) {
      const name = this.selectedMenu.name
      const date = this.days.find(d => d.name === name).date.format('YYYY-MM-DD')
      const menu = {
        id: this.selectedMenu.id || uuidv4(),
        option_four: options.four,
        option_three: options.three,
        option_two: options.two,
        option_one: options.one,
        name: name,
        date
      }

      console.log(this.selectedMenu.created)
      let promise = Promise.resolve()
      if (this.selectedMenu.created) {
        promise = this.editMenu(menu)
      } else {
        promise = this.createMenu(menu)
      }
      promise.then(res => console.log('menu has submitted successfully'))
    }
  }
}
</script>

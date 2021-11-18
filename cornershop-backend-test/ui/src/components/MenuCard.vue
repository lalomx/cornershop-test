<template>
  <div class="overflow-hidden shadow-lg modal-menu" :class="open">
    <div class="bg-white px-6 py-4 max-w-sm rounded inner">
      <div class="flex font-bold text-xl mb-2 justify-between">
        <span>Edit menu</span>
        <span class="close" @click="close">Close</span>
      </div>
      <form class="px-8 pt-6 pb-8 mb-4">
        <div class="mb-4">
          <label
            class="block text-gray-700 text-sm font-bold mb-2"
            for="username"
          >
            Option 1
          </label>
          <input
            v-model="options.one"
            class="
              shadow
              appearance-none
              border
              rounded
              w-full
              py-2
              px-3
              text-gray-700
              leading-tight
              focus:outline-none focus:shadow-outline
            "
            id="one"
            type="text"
            placeholder="Option"
          />
        </div>
        <div class="mb-4">
          <label
            class="block text-gray-700 text-sm font-bold mb-2"
            for="two"
          >
            Option 2
          </label>
          <input
            v-model="options.two"
            class="
              shadow
              appearance-none
              border
              rounded
              w-full
              py-2
              px-3
              text-gray-700
              leading-tight
              focus:outline-none focus:shadow-outline
            "
            id="two"
            type="text"
            placeholder="Option"
          />
        </div>
        <div class="mb-4">
          <label
            class="block text-gray-700 text-sm font-bold mb-2"
            for="three"
          >
            Option 3
          </label>
          <input
            v-model="options.three"
            class="
              shadow
              appearance-none
              border
              rounded
              w-full
              py-2
              px-3
              text-gray-700
              leading-tight
              focus:outline-none focus:shadow-outline
            "
            id="three"
            type="text"
            placeholder="Option"
          />
        </div>
        <div class="mb-4">
          <label
            class="block text-gray-700 text-sm font-bold mb-2"
            for="four"
          >
            Option 4
          </label>
          <input
            v-model="options.four"
            class="
              shadow
              appearance-none
              border
              rounded
              w-full
              py-2
              px-3
              text-gray-700
              leading-tight
              focus:outline-none focus:shadow-outline
            "
            id="four"
            type="text"
            placeholder="Option"
          />
        </div>
        <div class="flex items-center justify-between">
          <button
            class="
              bg-blue-500
              hover:bg-blue-700
              text-white
              font-bold
              py-2
              px-4
              rounded
              focus:outline-none focus:shadow-outline
            "
            type="button"
            @click="submit"
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'MenuCard',
  props: ['enabled', 'menu'],
  data () {
    return {
      options: {}
    }
  },
  watch: {
    menu () {
      if (!this.menu || _.isEmpty(this.menu)) {
        return
      }
      this.$set(this.options, 'one', this.menu.option_one)
      this.$set(this.options, 'two', this.menu.option_two)
      this.$set(this.options, 'three', this.menu.option_three)
      this.$set(this.options, 'four', this.menu.option_four)
    }
  },
  computed: {
    open () {
      return this.enabled ? 'open' : ''
    }
  },
  methods: {
    close () {
      this.options = {}
      this.$emit('close')
    },
    submit () {
      this.$emit('submit', { ...this.options })
      this.close()
    }
  }
}
</script>

<style scoped>
.modal-menu {
  position: absolute;
  top: 0;
  left: 0;
  background-color: rgba(0,0,0,0.3);
  z-index: 2;
  width: 100%;
  height: 100%;
  display: none;
}

.modal-menu.open {
  display: block;
}

.modal-menu.open .close:hover {
  cursor: pointer;
}

.modal-menu .inner {
  position: relative;
  top: calc(50vh - 270px);
  left: calc(50vw - 195px);
}

.modal-menu form {
  height:100%
}
</style>

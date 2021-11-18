<template>
<div class="container mx-auto flex flex-col">
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
        Employees
      </h1>
    </div>
  <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
    <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
      <div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Name
              </th>
              <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                Channel
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <template v-if="employees && employees.length > 0">
              <tr v-for="emp in employees" :key="emp.id">
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="flex items-start">
                  <div class="ml-4">
                    <div class="text-sm font-medium text-gray-900">
                      {{ emp.first_name }} {{ emp.last_name }}
                    </div>
                    <div class="text-sm text-gray-500">
                      {{ emp.email }}
                    </div>
                  </div>
                </div>
              </td>
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm text-gray-900">Slack</div>
                <div class="text-sm text-gray-500">{{ emp.slack_id }}</div>
              </td>
            </tr>
            </template>
            <tr v-else>
              <td class="px-6 py-4 whitespace-nowrap">
                <div class="flex items-start">
                  <div class="ml-4">
                    <div class="text-sm font-medium text-gray-900">
                      No results
                    </div>
                  </div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import api from '../mixins/api.mixin'

export default {
  name: 'Employees',
  mixins: [api],
  data () {
    return {
      employees: []
    }
  },
  async created () {
    const { data: employees } = await this.getEmployees()
    this.employees = employees
  }
}
</script>

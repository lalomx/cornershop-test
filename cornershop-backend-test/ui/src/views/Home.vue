<template>
 <div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-2xl mx-auto py-16 sm:py-24 lg:py-32 lg:max-w-none">
        <h2 class="text-2xl font-extrabold text-gray-900">Welcome</h2>

        <div class="mt-6 space-y-12 lg:space-y-0 lg:grid lg:grid-cols-2 lg:gap-8">
          <div class="group relative">
            <div class="relative w-full h-80 bg-white rounded-lg overflow-hidden group-hover:opacity-75 sm:aspect-w-2 sm:aspect-h-1 sm:h-64 lg:aspect-w-1 lg:aspect-h-1">
              <img src="https://thumbs.dreamstime.com/b/people-eating-lunchboxes-grey-table-top-view-healthy-food-delivery-161242402.jpg" alt="Desk with leather desk pad, walnut desk organizer, wireless keyboard and mouse, and porcelain mug." class="w-full h-full object-center object-cover">
            </div>
            <h3 class="mt-6 text-sm text-gray-500">
              <router-link to="/menu">
                <span class="absolute inset-0"></span>
                Menu
              </router-link>
            </h3>
            <p class="text-base font-semibold text-gray-900">View Menus</p>
          </div>

          <div class="group relative">
            <div class="relative w-full h-80 bg-white rounded-lg overflow-hidden group-hover:opacity-75 sm:aspect-w-2 sm:aspect-h-1 sm:h-64 lg:aspect-w-1 lg:aspect-h-1">
              <img src="https://www.eatthis.com/wp-content/uploads/sites/4/2020/12/fast-food-2020.jpg?quality=82&strip=1&resize=640%2C360" alt="Wood table with porcelain mug, leather journal, brass pen, leather key ring, and a houseplant." class="w-full h-full object-center object-cover">
            </div>
            <h3 class="mt-6 text-sm text-gray-500">
              <router-link to="/orders">
                <span class="absolute inset-0"></span>
                Orders
              </router-link>
            </h3>
            <p class="text-base font-semibold text-gray-900">View orders</p>
          </div>

          <div class="group relative">
            <div class="relative w-full h-80 bg-white rounded-lg overflow-hidden group-hover:opacity-75 sm:aspect-w-2 sm:aspect-h-1 sm:h-64 lg:aspect-w-1 lg:aspect-h-1">
              <img src="https://p1.pxfuel.com/preview/198/34/390/coding-macbook-laptop-computer-keyboard-code.jpg" alt="Wood table with porcelain mug, leather journal, brass pen, leather key ring, and a houseplant." class="w-full h-full object-center object-cover">
            </div>
            <h3 class="mt-6 text-sm text-gray-500">
              <router-link to="/employees">
                <span class="absolute inset-0"></span>
                Employees
              </router-link>
            </h3>
            <p class="text-base font-semibold text-gray-900">View employees</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>
<style scoped>
</style>

<template>

  <div class="section">
    <br>
    <br>
    <br>
    <br>
    <div class="clearfix">
      <h2>Comments</h2>
    </div>


    <div v-for="comment in comments" :key="comment">
      <div class="item_comment">
        <h4>User: {{ comment.username }}</h4>
        <h4>Company: {{ comment.company }}</h4>
        <h4 class="date">{{ comment.created_date.slice(0, 10) }}</h4>

        <div class="description">
          <p>{{ comment.text }}</p>
        </div><!-- description end -->

      </div><!-- item end -->

    </div>
  </div><!-- section end -->


</template>

<script>
export default {
  name: "Comments",
  props: ['comments']
}

</script>

<style scoped>

</style>
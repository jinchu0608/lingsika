<template>
  <section class="bio-section">
    <div class="bio-container">
      <div class="bio-avatar">
        <img :src="avatar" :alt="name" />
      </div>
      <h2 class="bio-name">{{ name }}</h2>
      <p class="bio-description">{{ description }}</p>
    </div>
  </section>
</template>

<script setup>
defineProps({
  avatar: {
    type: String,
    default: 'https://picsum.photos/seed/avatar/200/200'
  },
  name: {
    type: String,
    default: '摄影师'
  },
  description: {
    type: String,
    default: '热爱摄影，用镜头捕捉生活中的美好瞬间。'
  }
})
</script>

<style scoped>
.bio-section {
  padding: 100px 24px;
  background: #f8f8f8;
  text-align: center;
}

.bio-container {
  max-width: 600px;
  margin: 0 auto;
}

.bio-avatar {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  overflow: hidden;
  margin: 0 auto 24px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
}

.bio-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.bio-name {
  font-size: 28px;
  font-weight: 300;
  letter-spacing: 3px;
  color: #1a1a1a;
  margin: 0 0 16px;
}

.bio-description {
  font-size: 16px;
  color: #666;
  line-height: 1.8;
  letter-spacing: 0.5px;
  margin: 0;
}

@media (max-width: 768px) {
  .bio-section {
    padding: 60px 20px;
  }
  .bio-avatar {
    width: 100px;
    height: 100px;
  }
  .bio-name {
    font-size: 22px;
  }
}
</style>

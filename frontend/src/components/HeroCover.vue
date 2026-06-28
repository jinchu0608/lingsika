<template>
  <section class="hero-cover" :style="{ backgroundImage: `url(${bgImage})` }">
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <h1 class="hero-title">{{ title }}</h1>
      <p class="hero-subtitle" v-if="subtitle">{{ subtitle }}</p>
    </div>
  </section>
</template>

<script setup>
defineProps({
  bgImage: {
    type: String,
    default: 'https://picsum.photos/seed/hero/1920/1080'
  },
  title: {
    type: String,
    default: '摄影作品集'
  },
  subtitle: {
    type: String,
    default: '用镜头记录世界的美好'
  }
})
</script>

<style scoped>
.hero-cover {
  position: relative;
  width: 100%;
  height: 100vh;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    rgba(0, 0, 0, 0.2),
    rgba(0, 0, 0, 0.5)
  );
}

.hero-content {
  position: relative;
  z-index: 1;
  text-align: center;
  color: #fff;
  padding: 0 24px;
}

.hero-title {
  font-size: clamp(32px, 6vw, 72px);
  font-weight: 200;
  letter-spacing: 6px;
  margin: 0;
  line-height: 1.2;
}

.hero-subtitle {
  font-size: clamp(14px, 2vw, 20px);
  font-weight: 300;
  letter-spacing: 3px;
  margin-top: 20px;
  opacity: 0.75;
}
</style>

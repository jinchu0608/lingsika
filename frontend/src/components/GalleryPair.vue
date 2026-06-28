<template>
  <section class="gallery-section">
    <div class="gallery-container">
      <div v-for="(item, index) in items" :key="index" class="gallery-item">
        <div class="image-wrapper">
          <img :src="item.image" :alt="item.title" loading="lazy" />
        </div>
        <div class="caption">
          <h3 class="caption-title">{{ item.title }}</h3>
          <p class="caption-desc" v-if="item.description">{{ item.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({
  items: {
    type: Array,
    default: () => [
      {
        image: 'https://picsum.photos/seed/gallery1/800/600',
        title: '山水之间',
        description: '山川与流水的对话'
      },
      {
        image: 'https://picsum.photos/seed/gallery2/800/600',
        title: '城市光影',
        description: '都市中的光与影'
      }
    ]
  }
})
</script>

<style scoped>
.gallery-section {
  padding: 80px 24px;
  background: #fff;
}

.gallery-container {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
}

.gallery-item {
  display: flex;
  flex-direction: column;
}

.image-wrapper {
  width: 100%;
  overflow: hidden;
  border-radius: 4px;
}

.image-wrapper img {
  width: 100%;
  height: auto;
  display: block;
  transition: transform 0.4s ease;
}

.image-wrapper:hover img {
  transform: scale(1.03);
}

.caption {
  padding: 20px 4px 0;
}

.caption-title {
  font-size: 22px;
  font-weight: 400;
  letter-spacing: 1px;
  color: #1a1a1a;
  margin: 0 0 8px;
}

.caption-desc {
  font-size: 15px;
  color: #666;
  line-height: 1.6;
  letter-spacing: 0.3px;
  margin: 0;
}

@media (max-width: 768px) {
  .gallery-section {
    padding: 48px 16px;
  }
  .gallery-container {
    grid-template-columns: 1fr;
    gap: 32px;
  }
}
</style>

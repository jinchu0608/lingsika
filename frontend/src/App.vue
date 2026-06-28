<script setup>
import HeroCover from './components/HeroCover.vue'
import GalleryPair from './components/GalleryPair.vue'
import AuthorBio from './components/AuthorBio.vue'

const hero = {
  bgImage: 'https://picsum.photos/seed/photography-hero/1920/1080',
  title: '影像集',
  subtitle: '每一帧都是时光的标本'
}

const galleryItems = [
  {
    image: 'https://picsum.photos/seed/landscape/800/600',
    title: '山水之间',
    description: '山川与流水的对话，自然与宁静的交织'
  },
  {
    image: 'https://picsum.photos/seed/cityscape/800/600',
    title: '城市光影',
    description: '都市中的光与影，现代与传统的碰撞'
  }
]

const bio = {
  avatar: 'https://picsum.photos/seed/photographer/200/200',
  name: '金初',
  description: '热爱摄影，用镜头捕捉生活中的美好瞬间。足迹遍布山川湖海，记录不同文化背景下的人文故事。相信每一张照片都是一段时光的切片，值得被好好珍藏。'
}
</script>

<template>
  <div id="app-root">
    <HeroCover
      :bg-image="hero.bgImage"
      :title="hero.title"
      :subtitle="hero.subtitle"
    />
    <GalleryPair :items="galleryItems" />
    <AuthorBio
      :avatar="bio.avatar"
      :name="bio.name"
      :description="bio.description"
    />
  </div>
</template>

<style>
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
    'Helvetica Neue', Arial, 'Noto Sans SC', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background: #fff;
  color: #333;
}

#app-root {
  width: 100%;
  overflow-x: hidden;
}
</style>

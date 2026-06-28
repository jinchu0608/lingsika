<script setup>
import { ref, onMounted } from "vue"
import HeroCover from "./components/HeroCover.vue"
import GalleryPair from "./components/GalleryPair.vue"
import AuthorBio from "./components/AuthorBio.vue"
import {
  getCoverImage,
  getCoverText,
  getGalleryItems,
  getAuthorAvatar,
  getAuthorInfo,
} from "./api.js"

const hero = ref({ bgImage: "", title: "", subtitle: "" })
const galleryItems = ref([])
const bio = ref({ avatar: "", name: "", description: "" })
const loading = ref(true)

onMounted(async () => {
  try {
    const [img, txt, items, avatar, info] = await Promise.all([
      getCoverImage(),
      getCoverText(),
      getGalleryItems(),
      getAuthorAvatar(),
      getAuthorInfo(),
    ])
    hero.value = {
      bgImage: img.image_url,
      title: txt.title,
      subtitle: txt.subtitle,
    }
    galleryItems.value = items.map((i) => ({
      image: i.image_url,
      title: i.title,
      description: i.description,
    }))
    bio.value = {
      avatar: avatar.image_url,
      name: info.name,
      description: info.description,
    }
  } catch (e) {
    console.error("数据加载失败，使用默认值", e)
    hero.value = {
      bgImage: "https://picsum.photos/seed/photography-hero/1920/1080",
      title: "影像集",
      subtitle: "每一帧都是时光的标本",
    }
    galleryItems.value = [
      {
        image: "https://picsum.photos/seed/landscape/800/600",
        title: "山水之间",
        description: "山川与流水的对话，自然与宁静的交织",
      },
      {
        image: "https://picsum.photos/seed/cityscape/800/600",
        title: "城市光影",
        description: "都市中的光与影，现代与传统的碰撞",
      },
    ]
    bio.value = {
      avatar: "https://picsum.photos/seed/photographer/200/200",
      name: "金初",
      description: "热爱摄影，用镜头捕捉生活中的美好瞬间。",
    }
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div id="app-root" v-if="!loading">
    <HeroCover
      :bg-image="hero.bgImage"
      :title="hero.title"
      :subtitle="hero.subtitle"
    />
    <GalleryPair :items="galleryItems" v-if="galleryItems.length" />
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
    'Helvetica Neue', Arial, 'Noto Sans SC', 'Noto Sans CJK SC', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background: #fff;
  color: #333;
}

#app-root {
  width: 100%;
  overflow-x: hidden;
}

.loading {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  font-size: 18px;
  color: #999;
  letter-spacing: 2px;
}
</style>

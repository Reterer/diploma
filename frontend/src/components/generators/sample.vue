<template>
    <div v-html="item.public_data.question">
    </div>
    <div>
        {{ item.answer }}
        <div class="form-check" v-for="check in item.public_data.checks">
            <input class="form-check-input" type="checkbox" :value="check.id" v-model="answer">
            <label class="form-check-label">
                {{ check.text }}
            </label>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            answer: [],
        }
    },
    props: {
        item: Object,
    }
}
</script>


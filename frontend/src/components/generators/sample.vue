<template>
    <div v-html="item.public_data.question">
    </div>
    <div>
        {{ answer }}
        <div class="form-check" v-for="check in item.public_data.checks">
            <input class="form-check-input" type="checkbox" :value="check.id" v-model="answer" v-on:change="onChecked">
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
            answer: []
        }
    },
    props: {
        item: Object,
    },
    methods: {
        onChecked(e) {
            console.log("hi")
            this.$emit('answered', this.answer)
        }
    }
}
</script>


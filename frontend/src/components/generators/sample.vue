<template>
    <div v-html="item.question">
    </div>
    <div>
        <div class="form-check" v-for="check in item.checks">
            <input class="form-check-input" type="checkbox" :value="check.id" v-model="item.answer">
            <label class="form-check-label">
                {{ check.text }}
            </label>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        item: Object,
    },
}
</script>


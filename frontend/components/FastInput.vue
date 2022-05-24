<template>
    <div class="flex flex-col">
        <label for="">{{ title }}</label>
        <input
            :type="type"
            @input="input"
            :value="value"
            class="
                appearance-none
                block
                w-full
                bg-slate-100
                rounded
                py-3
                px-4
                mb-3
                leading-tight
                border-2 border-white
                focus:outline-none focus:bg-white focus:border-slate-500
            "
        />
    </div>
</template>

<script>
export default {
    props: {
        title: String,
        type: String,
        value: {
            type: undefined,
            default: '',
        },
    },

    methods: {
        input(e) {
            this.$emit('input', e.target.value)
        },
    },
}
</script>
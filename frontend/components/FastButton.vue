<template>
    <button
        @click="fn"
        type="button"
        class="
            bg-violet-500
            text-white
            py-2
            px-4
            rounded
            transition-all
            ease-linear
            delay-150
        "
    >
        <slot />
    </button>
</template>

<script>
export default {
    props: {
        fn: {
            type: Function,
            default: () => {},
        },
    },
}
</script>
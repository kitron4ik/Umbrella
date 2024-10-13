<template>
<div>
    <Headers/>
    <main>
            <slot>

            </slot>
    </main>
</div>
</template>

<script>
import Headers from './Headers/Headers.vue';

export default {
    components: {Headers}
}
</script>

<style>

</style>
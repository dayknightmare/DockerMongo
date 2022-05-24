<template>
    <form method="post" class="flex flex-row flex-wrap w-1/2">
        <fast-input
            class="w-1/2 p-2"
            :title="'Nome'"
            :type="'text'"
            v-model="name"
            :value="name"
        />
        <fast-input
            class="w-1/2 p-2"
            :title="'Idade'"
            :type="'number'"
            v-model="age"
            :value="age"
        />
        <fast-input
            class="w-1/2 p-2"
            :title="'Email'"
            :type="'email'"
            v-model="email"
            :value="email"
        />
        <fast-input
            class="w-1/2 p-2"
            :title="'Endereço'"
            :type="'text'"
            v-model="address"
            :value="address"
        />
        <fast-input
            class="w-1/2 p-2"
            :title="'CEP'"
            :type="'text'"
            v-model="zipCode"
            :value="zipCode"
        />
        <div class="flex flex-col w-1/2 p-2">
            <label for="">Sexo</label>
            <select
                v-model="sex"
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
                    focus:outline-none focus:bg-white
                "
            >
                <option value="">Selecione</option>
                <option value="m">Masculino</option>
                <option value="f">Feminino</option>
            </select>
        </div>
        <div class="p-2">
            <fast-button :fn="edit"> Editar </fast-button>
        </div>
    </form>
</template>

<script>
export default {
    data() {
        return {
            name: '',
            age: 0,
            email: '',
            address: '',
            zipCode: '',
            sex: '',
            id: this.$route.params.id,
        }
    },

    mounted() {
        this.getUser()
    },

    methods: {
        getUser() {
            this.$api.api.get(`/users/${this.id}`).then((re) => {
                this.name = re.data.name
                this.email = re.data.email
                this.address = re.data.address
                this.zipCode = re.data.zipCode
                this.age = re.data.age
                this.sex = re.data.sex.toLowerCase()
            })
        },

        edit() {
            this.$api.api
                .put(`/users/${this.id}`, {
                    name: this.name,
                    age: this.age,
                    email: this.email,
                    address: this.address,
                    zipCode: this.zipCode,
                    sex: this.sex,
                })
                .then(() => {
                    alert('Salvo com sucesso')
                    this.$router.push('/')
                })
        },
    },
}
</script>
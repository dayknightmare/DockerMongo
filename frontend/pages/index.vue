<template>
    <div>
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
                <fast-button :fn="add"> Enviar </fast-button>
            </div>
        </form>
        <br />
        <div class="p-2">
            <h4 class="text-2xl text-slate-700">Usuários</h4>
            <br />
            <div
                v-for="i in users"
                :key="i._id"
                class="
                    border-b-2 border-slate-100
                    py-2
                    flex flex-row
                    justify-between
                "
            >
                <div>
                    <p>{{ i.name }} | idade: {{ i.age }} | {{ i.email }}</p>
                    <span class="text-gray-600 font-thin">
                        {{ i.address }} - {{ i.zipCode }}
                    </span>
                    <br />
                </div>

                <div class="flex flex-row">
                    <fast-button class="mr-4" :fn="() => deleteUser(i._id)">
                        Apagar
                    </fast-button>
                    <fast-button :fn="() => $router.push(`/${i._id}`)">
                        Editar
                    </fast-button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import FastInput from '~/components/FastInput.vue'
import FastButton from '~/components/FastButton.vue'
export default {
    components: { FastInput, FastButton },

    data() {
        return {
            name: '',
            age: 0,
            email: '',
            address: '',
            zipCode: '',
            sex: '',
            users: [],
        }
    },

    mounted() {
        this.getUser()
    },

    methods: {
        getUser() {
            this.$api.api.get('/users').then((re) => {
                this.users = re.data
            })
        },

        deleteUser(id) {
            if (confirm('Deseja apagar este usuário?')) {
                this.$api.api.delete(`/users/${id}`).then(() => {
                    window.location.reload()
                })
            }
        },

        add() {
            this.$api.api
                .post('/user', {
                    name: this.name,
                    age: this.age,
                    email: this.email,
                    address: this.address,
                    zipCode: this.zipCode,
                    sex: this.sex,
                })
                .then(() => {
                    alert('Salvo com sucesso')
                    this.name = ''
                    this.age = 0
                    this.email = ''
                    this.address = ''
                    this.zipCode = ''
                    this.sex = ''
                    this.getUser()
                })
        },
    },
}
</script>



